#!/usr/bin/env python3
"""2-lifo_cache
A dictionary to illustrate LIFO
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None  # To keep track of the last key added

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                self.cache_data.pop(self.last_key)
                print(f"DISCARD: {self.last_key}")

        self.last_key = key  # Update the last key added

    def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key) if key is not None else None
