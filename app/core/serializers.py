from rest_framework import serializers

class FibonacciSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=1, max_value=99999)