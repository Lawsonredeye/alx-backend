#!/usr/bin/env python3
"""
LRUCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dict self.cache_data the item value for the key key

        Args:
            key: str or int value which acts as id
            item: str or int value which would be stored as key value
        """
        

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