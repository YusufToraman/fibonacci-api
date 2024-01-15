""" Fibonacci view will be written in this file."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import FibonacciSerializer
from core.helpers.CacheFactory import CacheFactory

def fibonacci(n):
    """Return the n-th value from the Fibonacci sequence."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

class FibonacciView(APIView):
    """Fibonacci view."""

    def get(self, request):
        """Get request to calculate the n-th Fibonacci number."""

        # Get the redis instance from the factory
        redis_instance = CacheFactory.get_cache('redis', host='redis', port=6379, db=0) # cache type and kwargs => dict
        serializer = FibonacciSerializer(data = request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Get the validated data
        n = serializer.validated_data['n']
        cache_key = f'fib_{n}'

        # If the cache key exists, return the value from the cache, if not exist => falsy value => None
        if redis_instance.get(cache_key):
            res = redis_instance.get(cache_key)
            return Response({'result': int(res)}, status=status.HTTP_200_OK)

        res = fibonacci(n)
        # Set the value in the cache
        redis_instance.set(cache_key, str(res), timeout=60*60*24) # 1 day cache
        return Response({'result': int(res)}, status=status.HTTP_200_OK)