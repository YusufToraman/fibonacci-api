""" Fibonacci view will be written in this file."""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.serializers import FibonacciSerializer
from core.helpers.CacheFactory import CacheFactory
from core.operations.CachedOperations import CachedOperations


class FibonacciView(APIView):
    """Fibonacci view."""

    def get(self, request):
        """Get request to calculate the n-th Fibonacci number."""

        # Get the redis instance from the factory
        redis_instance = CacheFactory.get_cache(
            'redis', 
            host='redis', 
            port=6379, 
            db=0
        )  # cache type and parameters"""

        serializer = FibonacciSerializer(data = request.query_params)
        if not serializer.is_valid():
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Get the validated data
        n = serializer.validated_data['n']
        cache_key = f'fib_{n}'

        res = CachedOperations(
            'fibonacci',
            redis_instance, 
            cache_key,
            n
        ).check_cache()

        return Response({'result': int(res)}, status=status.HTTP_200_OK)


class DeploymentUpdate(APIView):
    """Deployment update view."""

    def get(self, request):
        """Get request to update the deployment."""
        return Response({'Deployment Update': 'True'}, status=status.HTTP_200_OK)