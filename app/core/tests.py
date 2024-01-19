from django.test import SimpleTestCase
from rest_framework.test import APIClient
from core.operations.fibonacci import Fibonacci
from core.helpers.RedisCache import RedisCache

class TestFibonacci(SimpleTestCase):

    def test_fibonacci_calculation(self):
        """Unit test for fibonacci calculation"""
        fib = Fibonacci(10)
        result = fib.calculate()
        self.assertEqual(result, 55)

    def test_redis_cache_set(self):
        """Unit test for redis cache set and get method"""
        cache = RedisCache('redis', 6379, 0)
        cache.set('test_key', 'test_value')
        value = cache.get('test_key').decode('utf-8')
        self.assertEqual(value, 'test_value')

    def test_invalid_parameter(self):
        """Integration test for invalid parameter"""
        client = APIClient()
        res = client.get('/api/calc-fib/', {'n': -5})
        self.assertEqual(res.status_code, 400)

    def test_fibonacci_caching(self):
        """Integration test for fibonacci caching"""
        client = APIClient()
        first_res = client.get('/api/calc-fib/', {'n': 10})
        second_res = client.get('/api/calc-fib/', {'n': 10})
        self.assertEqual(first_res.data, second_res.data)

    def test_get_fibonacci(self):
        """Integration test for fibonacci API"""
        client = APIClient()
        res = client.get('/api/calc-fib/', {'n': 13})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            {'result': 233}
        )