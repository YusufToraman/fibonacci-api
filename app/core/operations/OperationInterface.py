from abc import ABC, abstractmethod  # Abstract Base Class imports

class OperationInterface(ABC):
    @abstractmethod
    def calculate(self, n):
        pass