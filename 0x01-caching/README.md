# Caching

> This project was Caching.

## Summary

I learnt about what a caching system is, `FIFO`, `LIFO`, `LRU`, `MRU`, `LFU`, the purpose of a caching system, and the limits a caching system has.

## Files

> Each file contains the solution to a task in the project.

- All classes must inherit from `BaseCaching` defined below:
```py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```
- [ ] [0-basic_cache.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/0-basic_cache.py): A class `BasicCache` that inherits from `BaseCaching` and is a caching system.
- [ ] [1-fifo_cache.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/1-fifo_cache.py): A class `FIFOCache` that inherits from `BaseCaching` and is a caching system.
- [ ] [2-lifo_cache.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/2-lifo_cache.py): A class `LIFOCache` that inherits from `BaseCaching` and is a caching system.
- [ ] [3-lru_cache.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/3-lru_cache.py): A class `LRUCache` that inherits from `BaseCaching` and is a caching system.
- [ ] [4-mru_cache.py](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/4-mru_cache.py): A class `MRUCache` that inherits from `BaseCaching` and is a caching system.
- [ ] [](https://github.com/Ebube-Ochemba/alx-backend/blob/main/0x01-caching/):

> [test_files](): A folder of test files. Provided by Alx.
