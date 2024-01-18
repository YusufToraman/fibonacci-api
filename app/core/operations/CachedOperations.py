from core.helpers.CacheInterface import CacheInterface
from core.operations.OperationFactory import OperationFactory
from rest_framework.response import Response
from rest_framework import status

class CachedOperations:
    def __init__(self, operation_type: str, cache: CacheInterface, cache_key: str, n: int):
        self.cache = cache
        self.n = n
        self.cache_key = cache_key
        self.operation_type = operation_type

    def check_cache(self):
        # Check if the value is in the cache
        if self.cache.get(self.cache_key):
            res = self.cache.get(self.cache_key)
            return int(res)
        # If the value is not in the cache, calculate it and set it in the cache
        else:
            res = OperationFactory.get_operation(
                self.operation_type, 
                self.n
            ).calculate()
            self.cache.set(self.cache_key, str(res), timeout=60 * 60 * 24)  # 1 day cache
            return int(res)
