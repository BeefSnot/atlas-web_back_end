#!/usr/bin/env python3
"""2-lifo_cache module.

Provides LIFOCache implementing a Last-In First-Out eviction policy.
"""
from typing import Any, List
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache: cache with LIFO eviction policy."""

    def __init__(self) -> None:
        """Initialize the cache and a stack to track insertion order."""
        super().__init__()
        self._stack: List[Any] = []

    def put(self, key: Any, item: Any) -> None:
        """Add an item in the cache using LIFO eviction when needed.

        - If key or item is None, do nothing.
        - On new key insertion, push key to stack; if key exists, just update value
          and do not change stack order.
        - If exceeding MAX_ITEMS after insertion of a new key, discard the most
          recently inserted key prior to this insertion (the previous top of stack),
          print 'DISCARD: <key>'. If duplicate keys exist in stack, clean them lazily.
        """
        if key is None or item is None:
            return

        is_new_key = key not in self.cache_data
        self.cache_data[key] = item
        if is_new_key:
            self._stack.append(key)
        else:
            self._stack.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            current = self._stack.pop() 
            discard = None
            while self._stack:
                candidate = self._stack.pop()
                if candidate in self.cache_data:
                    discard = candidate
                    break
            self._stack.append(current)
            if discard is not None and discard in self.cache_data:
                del self.cache_data[discard]
                print(f"DISCARD: {discard}")

    def get(self, key: Any) -> Any:
        """Return the value linked to `key` or None if absent."""
        if key is None:
            return None
        return self.cache_data.get(key)
