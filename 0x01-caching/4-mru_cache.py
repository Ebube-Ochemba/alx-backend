#!/usr/bin/env python3
"""4-mru_cache
A dictionary to illustrate MRU
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []  # To keep track of the order of usage

    def put(self, key, item):
        """Add an item to the cache with MRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, update the order...
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)  # Mark the key as the most recently used

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict the most recently used item
            mru_key = self.usage_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)  # Mark the key as the most recently used
        return self.cache_data[key]
