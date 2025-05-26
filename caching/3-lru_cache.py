#!/usr/bin/env python3
"""LRU caching system implementation"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache that discards least recently used items"""

    def __init__(self):
        """Initialize cache system"""
        super().__init__()
        self.access_order = []  # Track access history

    def put(self, key, item):
        """Add item to cache with LRU replacement policy"""
        if not key or not item:
            return

        # Update access history for existing keys
        if key in self.access_order:
            self.access_order.remove(key)
        
        # Append to track as most recently used
        self.access_order.append(key)
        
        # Handle eviction if cache is full
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and 
                key not in self.cache_data):
            # Remove least recently used item (front of list)
            lru = self.access_order.pop(0)
            del self.cache_data[lru]
            print(f"DISCARD: {lru}")
            
        # Store item
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item and update access history"""
        if not key or key not in self.cache_data:
            return None
            
        # Update access history
        self.access_order.remove(key)
        self.access_order.append(key)
        
        return self.cache_data[key]
    