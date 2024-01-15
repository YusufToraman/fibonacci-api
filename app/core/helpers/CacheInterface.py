from abc import ABC, abstractmethod # Abstract Base Class imports

# Factory Design pattern will ve used to create the cache object, there could be more than 1 cache type, dynamically
# user can instantiate redis cache, x cache or y cache.

class CacheInterface(ABC):
    @abstractmethod
    # get method gets the value according to the key
    def get(self, key):
        pass

    def set(self, key, value, timeout = None):
        pass

    def delete(self, key):
        pass