#!/usr/bin/env python3
"""0-basic_cache
A Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A Class that defines a caching system"""
    def __init__(self):
        """Initialize the cache"""
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is not None:
            return self.cache_data.get(key)
        return None
