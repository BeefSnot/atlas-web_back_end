#!/usr/bin/env python3
"""1-fifo_cache module.

Provides FIFOCache implementing a First-In First-Out eviction policy.
"""
from typing import Any, Deque
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache: cache with FIFO eviction policy."""

    def __init__(self) -> None:
        """Initialize the cache and a queue to track insertion order."""
        super().__init__()
        self._order: Deque[Any] = deque()

    def put(self, key: Any, item: Any) -> None:
        """Add an item in the cache using FIFO eviction when needed.

        - If key or item is None, do nothing.
        - On new key insertion, append key to order; if key exists, just update value
          and do not change order.
        - If exceeding MAX_ITEMS after insertion of a new key, discard the oldest key
          (leftmost in the deque), print 'DISCARD: <key>'.
        """
        if key is None or item is None:
            return

        is_new_key = key not in self.cache_data
        self.cache_data[key] = item

        if is_new_key:
            self._order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self._order.popleft()
                if discard in self.cache_data:
                    del self.cache_data[discard]
                    print(f"DISCARD: {discard}")

    def get(self, key: Any) -> Any:
        """Return the value linked to `key` or None if absent."""
        if key is None:
            return None
        return self.cache_data.get(key)
