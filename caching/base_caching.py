#!/usr/bin/env python3
"""BaseCaching module.

Defines the base class for caching systems, including a default
maximum number of items and the storage dictionary.
"""


class BaseCaching:
    """BaseCaching defines:
    - a constant MAX_ITEMS, defaulting to 4
    - the cache storage dictionary `cache_data`
    """

    MAX_ITEMS = 4

    def __init__(self) -> None:
        """Initialize the cache storage."""
        self.cache_data = {}

    def print_cache(self) -> None:
        """Print the current cache content in sorted key order."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item) -> None:
        """Add an item in the cache.

        This method must be implemented by subclasses.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key.

        This method must be implemented by subclasses.
        """
        raise NotImplementedError("get must be implemented in your cache class")
