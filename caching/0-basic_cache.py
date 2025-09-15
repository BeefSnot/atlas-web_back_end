#!/usr/bin/env python3
"""0-basic_cache module.

Provides a BasicCache class that stores key/value pairs in a simple
unbounded dictionary without any eviction policy.
"""

from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache: basic unbounded caching system.

    Uses the inherited `cache_data` dict for storage.
    """

    def put(self, key: Any, item: Any) -> None:
        """Add an item in the cache.

        If `key` or `item` is None, do nothing. Otherwise, assign the
        item to `self.cache_data[key]`.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """Return the value linked to `key` in the cache.

        If `key` is None or not present, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
