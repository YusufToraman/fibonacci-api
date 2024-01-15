from django.urls import path
from core.views import FibonacciView

urlpatterns = [
    path('calc-fib/', FibonacciView.as_view(), name='calc-fib'),
]