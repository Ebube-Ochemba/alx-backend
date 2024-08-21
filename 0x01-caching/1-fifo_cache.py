#!/usr/bin/env python3
"""1-fifo_cache
A dictionary to illustrate FIFO
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If the key already exists, update the order...
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)  # Add key to the end of the order list

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # If the cache exceeds MAX_ITEMS, evict the first item added (FIFO)
            first_key = self.order.pop(0)  # remove 1st item in the order list
            del self.cache_data[first_key]  # Remove it from the cache
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieve an item from the cache"""
        return self.cache_data.get(key) if key is not None else None
