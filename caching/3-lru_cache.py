#!/usr/bin/env python3
"""3-lru_cache module.

Provides LRUCache implementing a Least Recently Used eviction policy.
"""
from typing import Any, OrderedDict as _OrderedDictType
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache: cache with LRU eviction policy.

    Uses an OrderedDict to track access order: most recent at end.
    """

    def __init__(self) -> None:
        """Initialize the cache using an OrderedDict for order tracking."""
        super().__init__()
        self.cache_data: _OrderedDictType[Any, Any] = OrderedDict()

    def put(self, key: Any, item: Any) -> None:
        """Add an item in the cache using LRU eviction when needed.

        - If key or item is None, do nothing.
        - On update of an existing key, move it to end (most recent).
        - On new insertion exceeding MAX_ITEMS, popitem(last=False) to discard LRU
          and print the discarded key.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.cache_data[key] = item
        else:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {discard}")

    def get(self, key: Any) -> Any:
        """Return the value linked to `key`, updating recency.

        If key is present, move it to end (most recent) and return value.
        Else return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data.get(key)
