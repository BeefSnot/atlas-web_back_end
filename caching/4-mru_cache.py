#!/usr/bin/env python3
"""4-mru_cache module.

Provides MRUCache implementing a Most Recently Used eviction policy.
"""
from typing import Any, OrderedDict as _OrderedDictType
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache: cache with MRU eviction policy.

    Tracks recency using an OrderedDict: most recent at end.
    """

    def __init__(self) -> None:
        """Initialize the cache using an OrderedDict for order tracking."""
        super().__init__()
        self.cache_data: _OrderedDictType[Any, Any] = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """Add an item in the cache using MRU eviction when needed.

        - If key or item is None, do nothing.
        - On update of an existing key, move it to end (most recent) and update.
        - On new insertion exceeding MAX_ITEMS, discard the most recently used
          existing item (popitem(last=True)) and print the discarded key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {discard}")
        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """Return the value linked to `key`, updating recency.

        If key is present, move it to end (most recent) and return value.
        Else return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
