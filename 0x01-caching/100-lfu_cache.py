#!/usr/bin/env python3
"""100-lfu_cache
A dictionary to illustrate LFU
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        super().__init__()
        self.usage_frequency = {}  # Tracks frequency of each key
        self.usage_order = {}      # Tracks the order of access
        self.time_stamp = 0        # Simulates time for LRU

    def put(self, key, item):
        """Add an item to the cache with LFU eviction"""
        if key is None or item is None:
            return

        # Increment timestamp for each operation
        self.time_stamp += 1

        if key in self.cache_data:
            # Update item and frequency if the key is already in cache
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order[key] = self.time_stamp
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU item (tie broken by LRU)
                lfu_key = min(self.usage_frequency,
                              key=lambda k: (self.usage_frequency[k],
                                             self.usage_order[k]))
                print(f"DISCARD: {lfu_key}")
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                del self.usage_order[lfu_key]

            # Add the new item
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order[key] = self.time_stamp

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        # Increment frequency and update order
        self.usage_frequency[key] += 1
        self.time_stamp += 1
        self.usage_order[key] = self.time_stamp

        return self.cache_data[key]
