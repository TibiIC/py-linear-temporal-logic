from abc import ABC, abstractmethod
from typing import Any


# Base class for LTL formulas
class LTLFormula(ABC):
    @abstractmethod
    def __str__(self):
        pass

    def format(self, formatter):
        """Format the formula using a provided formatter strategy."""
        return formatter.format(self)

    @staticmethod
    def parse(input_data, parser):
        """Parse an input (string, JSON, etc.) into an LTL formula using a given parser strategy."""
        return parser.parse(input_data)


class AtomicProposition(LTLFormula):
    def __init__(self, name: str, value: Any = None):
        self.name = name  # The name of the atomic proposition (e.g., "p", "q")
        self.value = value  # This can be either bool, int, or None

    def __str__(self):
        return f"{self.name}={self.value}" if self.value is not None else self.name

    def evaluate(self):
        """Evaluate the value of the atomic proposition.

        This method can be extended to include evaluation logic
        based on the value type.
        """
        if isinstance(self.value, bool):
            return self.value  # Return the boolean value
        elif isinstance(self.value, int):
            return self.value  # Return the integer value
        else:
            raise ValueError(f"Unsupported value type for atomic proposition: {type(self.value)}")

    def __repr__(self):
        return f"AtomicProposition(name={self.name}, value={self.value})"

    def set_value(self, value):
        """Set a new value for the atomic proposition."""
        self.value = value


# Logical operators
class Not(LTLFormula):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"¬({self.formula})"


class And(LTLFormula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∧ {self.right})"


class Or(LTLFormula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} ∨ {self.right})"


class Implies(LTLFormula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} → {self.right})"


# Temporal operators
class Next(LTLFormula):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"◯({self.formula})"


class Globally(LTLFormula):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"□({self.formula})"


class Eventually(LTLFormula):
    def __init__(self, formula):
        self.formula = formula

    def __str__(self):
        return f"◇({self.formula})"


class Until(LTLFormula):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left} U {self.right})"
