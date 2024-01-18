from .OperationInterface import OperationInterface

class Fibonacci(OperationInterface):
    def __init__(self, n):
        self.n = n

    def calculate(self):
        """Return the n-th value from the Fibonacci sequence."""
        a, b = 0, 1
        for _ in range(self.n):
            a, b = b, a + b
        return a
        
