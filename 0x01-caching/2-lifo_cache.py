#!/usr/bin/env python3
"""Module which simulates the FIFO caching policy and operations

Inherits from the BaseCaching class and extends it's functionality
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Performs FIFO mode of caching operations with important methods
    which fetchs and insert data into the cached dict storage
    """
    def __init__(self):
        """initialize the subclass from data of the base class
        """
        super().__init__()

    def put(self, key, item):
        """assign to the dict self.cache_data the item value for the key key

        Args:
            key: str or int value which acts as id
            item: str or int value which would be stored as key value
        """
        if key in self.cache_data.keys():
            self.cache_data[key] = item
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:

            # Create a list comprehension to get the keys
            new_cache = [x for x in self.cache_data.keys()]
            discarded = new_cache[-1]

            # Create a new dict to store the new key-values except the first
            # key-value in the cache_data dict
            new_dict = {
                x: d
                for x, d in self.cache_data.items()
                if x != discarded
                        }
            new_dict[key] = item
            self.cache_data = new_dict
            print(f"DISCARD: {discarded[0]}")

        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
            key: str or int which is used to fetch the value

        Returns:
            value of the cached key
        """
        if key is None or self.cache_data.get(key, None) is None:
            return None
        return self.cache_data.get(key)
