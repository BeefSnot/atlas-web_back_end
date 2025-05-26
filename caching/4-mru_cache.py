#!/usr/bin/env python3
"""MRU caching system implementation"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache that removes most recently used items when full"""

    def __init__(self):
        """Set up cache tracking"""
        super().__init__()
        self.usage_list = []  # Track item usage

    def put(self, key, item):
        """Store item using MRU eviction strategy"""
        if key is None or item is None:
            return

        # If updating existing item, refresh its position
        if key in self.usage_list:
            self.usage_list.remove(key)

        # Make this the most recently used item
        self.usage_list.append(key)

        # Handle cache overflow
        if (key not in self.cache_data and
                len(self.cache_data) >= self.MAX_ITEMS):
            # The most recently used item is the second-to-last in our list
            # (last is the current one we're adding)
            mru = self.usage_list[-2]
            self.cache_data.pop(mru)
            self.usage_list.remove(mru)
            print(f"DISCARD: {mru}")

        # Add to cache
        self.cache_data[key] = item

    def get(self, key):
        """Get item and update usage tracking"""
        if key not in self.cache_data:
            return None

        # Update usage tracking
        self.usage_list.remove(key)
        self.usage_list.append(key)

        return self.cache_data[key]
