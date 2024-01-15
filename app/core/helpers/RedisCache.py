from .CacheInterface import CacheInterface
import redis
from django.core.cache import cache

class RedisCache(CacheInterface):  # RedisCache class implements CacheInterface
    """RedisCache is a one product of factory as I understand"""
    def __init__(self, host, port, db=0):
        """Initialize the redis cache."""
        self.redis_instance = redis.StrictRedis(host=host, port=port, db=db)

    # ABC class forces to implement the abstract methods
    def get(self, key):
        """Get the value from redis cache."""
        # It calls the get method of redis instance
        return self.redis_instance.get(key)

    def set(self, key, value, timeout=None):
        """Set the value in redis cache."""
        # It calls the set method of redis instance
        self.redis_instance.set(key, value, timeout)

    def delete(self, key):
        """Delete the value from redis cache."""
        # It calls the delete method of redis instance
        self.redis_instance.delete(key)