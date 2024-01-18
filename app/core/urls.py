from django.urls import path
from core.views import FibonacciView, DeploymentUpdate

urlpatterns = [
    path('calc-fib/', FibonacciView.as_view(), name='calc-fib'),
    path('deployment-update/', DeploymentUpdate.as_view(), name='deployment-update')
]