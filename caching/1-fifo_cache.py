#!/usr/bin/env python3
"""
First-In-First-Out (FIFO) caching module
Implements a caching system that evicts the oldest entries first
"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFO Cache implementation that removes the oldest items when full.
    Uses OrderedDict to maintain insertion order of cache entries.
    """

    def __init__(self):
        """Set up the FIFO cache structure"""
        super().__init__()
        # Use OrderedDict to track insertion order
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add or update an item in the cache using FIFO policy

        Parameters:
            key: The lookup key for the item
            item: The value to store

        If cache is full, removes the first item that was added
        """
        if key is None or item is None:
            return

        # Add the new item
        self.cache_data[key] = item

        # Check if we need to remove the oldest item
        if len(self.cache_data) > self.MAX_ITEMS:
            # Get first key (oldest item)
            oldest_key, _ = next(iter(self.cache_data.items()))

            # Remove it
            self.cache_data.pop(oldest_key)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item from the cache

        Parameters:
            key: The key to look up

        Returns:
            The cached item or None if not found
        """
        if key is None:
            return None

        return self.cache_data.get(key)
    