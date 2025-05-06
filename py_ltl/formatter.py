from abc import ABC, abstractmethod

class ILTLFormatter(ABC):
    @abstractmethod
    def format(self, formula: 'LTLFormula') -> str:
        pass