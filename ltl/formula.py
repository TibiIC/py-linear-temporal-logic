from abc import ABC, abstractmethod

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

# Atomic proposition
class AtomicProposition(LTLFormula):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

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