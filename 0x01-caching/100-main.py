#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()

# Add some items
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(f"CURRENT USE ORDER 1: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 1: {my_cache.usage_frequency}")

# Access B to increase its frequency
print(my_cache.get("B"))
my_cache.print_cache()
print(f"CURRENT USE ORDER 2: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 2: {my_cache.usage_frequency}")

# Add E and trigger eviction
my_cache.put("E", "Battery")
my_cache.print_cache()
print(f"CURRENT USE ORDER 3: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 3: {my_cache.usage_frequency}")

# Update C and trigger eviction
my_cache.put("C", "Street")
my_cache.print_cache()
print(f"CURRENT USE ORDER 4: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 4: {my_cache.usage_frequency}")

# Access various items and print their frequencies
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.print_cache()
print(f"CURRENT USE ORDER 5: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 5: {my_cache.usage_frequency}")

# Continue to add items and observe eviction patterns
my_cache.put("F", "Mission")
my_cache.print_cache()
print(f"CURRENT USE ORDER 6: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 6: {my_cache.usage_frequency}")

my_cache.put("G", "San Francisco")
my_cache.print_cache()
print(f"CURRENT USE ORDER 7: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 7: {my_cache.usage_frequency}")

# Add more items to fill up cache and cause more evictions
my_cache.put("H", "H")
my_cache.print_cache()
print(f"CURRENT USE ORDER 8: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 8: {my_cache.usage_frequency}")

my_cache.put("I", "I")
my_cache.print_cache()
print(f"CURRENT USE ORDER 9: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 9: {my_cache.usage_frequency}")

# Access some items multiple times to increase their frequency
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.print_cache()
print(f"CURRENT USE ORDER 10: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 10: {my_cache.usage_frequency}")

# Add final items and trigger evictions
my_cache.put("J", "J")
my_cache.print_cache()
print(f"CURRENT USE ORDER 11: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 11: {my_cache.usage_frequency}")

my_cache.put("K", "K")
my_cache.print_cache()
print(f"CURRENT USE ORDER 12: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 12: {my_cache.usage_frequency}")

my_cache.put("L", "L")
my_cache.print_cache()
print(f"CURRENT USE ORDER 13: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 13: {my_cache.usage_frequency}")

my_cache.put("M", "M")
my_cache.print_cache()
print(f"CURRENT USE ORDER 14: {my_cache.usage_order}")
print(f"FREQUENCY COUNTS 14: {my_cache.usage_frequency}")
