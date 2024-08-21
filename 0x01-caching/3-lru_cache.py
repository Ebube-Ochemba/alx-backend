#!/usr/bin/env python3
"""3-lru_cache
A dictionary to illustrate LRU
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []  # To keep track of the order of usage

    def put(self, key, item):
        """Add an item to the cache with LRU eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, update the order...
            self.usage_order.remove(key)

        self.cache_data[key] = item
        self.usage_order.append(key)  # Mark the key as most recently used

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict the least recently used item
            lru_key = self.usage_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update usage order
        self.usage_order.remove(key)
        self.usage_order.append(key)  # Mark the key as the most recently used
        return self.cache_data[key]
