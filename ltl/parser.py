from abc import ABC, abstractmethod


class ILTLParser(ABC):
    """Abstract parser strategy interface."""

    @abstractmethod
    def parse(self, input_data):
        pass


