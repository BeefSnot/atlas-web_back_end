#!/usr/bin/env python3
"""
A streamlined cache module that provides basic data storage
with no size restrictions or eviction policies.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A straightforward caching implementation without size limitations.
    Extends the BaseCaching class to provide simple key-value storage.
    """

    def __init__(self):
        """Constructor: sets up the cache storage"""
        # Initialize parent class
        super().__init__()

    def put(self, key, item):
        """
        Store a value in the cache dictionary.

        Arguments:
            key: The identifier for the cached item
            item: The data to be stored
        """
        # Skip operations for invalid inputs
        if key is None or item is None:
            return

        # Store the item in the cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve a value from the cache.

        Arguments:
            key: The identifier to look up

        Returns:
            The stored value or None if not found
        """
        # Return None for invalid key
        if not key:
            return None

        # Fetch from cache dictionary
        return self.cache_data.get(key)