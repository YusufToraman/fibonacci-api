from .RedisCache import RedisCache

class CacheFactory:
    """CacheFactory is a factory class to create cache instance w.r.t cache string type"""
    def get_cache(cache_type, host, port, db=1):
        # There is 1 cache type yet, but there could be more than 1 cache type
        if cache_type == 'redis':
            return RedisCache(host, port, db)
        else:
            raise ValueError(f'Unknown cache type: {cache_type}')