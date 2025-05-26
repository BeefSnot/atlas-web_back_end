#!/usr/bin/env python3
"""
Last-In-First-Out (LIFO) caching system
Implements a stack-like cache that discards the most recently added item
when the cache reaches capacity
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache implementation - newest items are removed first when full.
    Tracks the most recently added key for eviction purposes.
    """

    def __init__(self):
        """Initialize the LIFO cache tracking system"""
        super().__init__()
        # Track the most recently added key
        self.most_recent = None

    def put(self, key, item):
        """
        Store or update an item in the cache using LIFO eviction policy

        Args:
            key: Identifier for cached data
            item: Value to be stored

        When cache reaches capacity, removes the most recently added item
        """
        if key is None or item is None:
            return

        # Handle cache at capacity
        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            # Remove the most recently added item
            if self.most_recent:
                evicted = self.most_recent
                del self.cache_data[evicted]
                print(f"DISCARD: {evicted}")

        # Store the new item and track it as most recent
        self.cache_data[key] = item
        self.most_recent = key

    def get(self, key):
        """
        Fetch a value from the cache by its key

        Args:
            key: The identifier to search for

        Returns:
            The cached value or None if not found
        """
        if not key:
            return None

        return self.cache_data.get(key)
    