from .fibonacci import Fibonacci

class OperationFactory:
    @staticmethod
    def get_operation(operation_type, n):
        if operation_type == 'fibonacci':
            return Fibonacci(n)  
        else:
            raise ValueError(f'Unknown operation type: {operation_type}')