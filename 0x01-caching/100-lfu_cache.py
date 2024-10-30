#!/usr/bin/python3
""" LFUCache module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Inherits from BaseCaching
      - Caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.count = {}
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
                self.count[key] += 1
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_value = min(self.count.values())
                all_keys = [
                    k for k in self.count if self.count[k] == min_value]
                discard = None
                if len(all_keys) == 1:
                    discard = all_keys[0]
                else:
                    for q in self.queue:
                        if q in all_keys:
                            discard = q
                            break
                self.queue.remove(discard)
                del self.cache_data[discard]
                del self.count[discard]
                self.count[key] = 0
                print("DISCARD: {}".format(discard))
            else:
                self.count[key] = 0
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.count[key] += 1
        return self.cache_data.get(key, None)
