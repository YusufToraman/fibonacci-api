from django.test import SimpleTestCase
from rest_framework.test import APIClient

class TestFibonacci(SimpleTestCase):
    def test_get_fibonacci(self):
        client = APIClient()
        res = client.get('/api/calc-fib/', {'n': 13})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.data,
            {'result': 233}
        )