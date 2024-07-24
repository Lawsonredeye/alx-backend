#!/usr/bin/env python3
"""Module for handling basic caching method
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Used as an extension of the BaseCaching class which has a method for
    storing data into the cache dict
    """
    def __init__(self):
        """Inherits from the BaseCaching class"""
        super().__init__()

    def put(self, key, item):
        """Stores data in a key-value pair format

        Args:
            key: string or int as a field to serve as a unique identity
            item: string or int as a value to be stored into a dict

        Returns:
            nothing
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetches data from the cache memory based on the key passed
        and returns None if Key doesn't exists

        Args:
            key: string, int value which would serve as an id for searching
            through the dict

        Returns:
            The value of the found key inside the dictionary
        """
        if key is None or self.cache_data.get(key, None) is None:
            return None
        return self.cache_data.get(key)
