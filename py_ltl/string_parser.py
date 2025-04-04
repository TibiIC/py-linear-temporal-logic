from pyparsing import Word, alphas, opAssoc, infixNotation

from py_ltl.formula import AtomicProposition, Not, And, Implies, Or, Until, Next, Globally, Eventually, Prev, Top, \
    Bottom
from py_ltl.parser import ILTLParser


class LTLStringParser(ILTLParser):
    """Parser for LTL formulas from strings using pyparsing."""

    def __init__(self):
        # Define atomic propositions (single-letter variables)
        self.operand = Word(alphas).setParseAction(self._parse_atomic)

        # Define operators
        self.operators = [
            # (op, precedence, associativity, function)
            ("⊤", 0, opAssoc.LEFT, self._parse_top),  # True
            ("⊥", 0, opAssoc.LEFT, self._parse_bottom),  # False
            ("¬", 1, opAssoc.RIGHT, self._parse_not),
            ("∧", 2, opAssoc.LEFT, self._parse_and),
            ("∨", 2, opAssoc.LEFT, self._parse_or),
            ("→", 2, opAssoc.RIGHT, self._parse_implies),  # Not implemented yet
            ("◯", 1, opAssoc.RIGHT, self._parse_next),
            ("P", 2, opAssoc.LEFT, self._parse_prev),
            ("□", 1, opAssoc.RIGHT, self._parse_globally),
            ("◇", 1, opAssoc.RIGHT, self._parse_eventually),
            ("U", 2, opAssoc.LEFT, self._parse_until),
        ]

        # Define the grammar using infix notation
        self.expression = infixNotation(
            self.operand,
            [(op, num, assoc, fn) for op, num, assoc, fn in self.operators]
        )

    def _parse_top(self, tokens):
        return Top()

    def _parse_bottom(self, tokens):
        return Bottom()

    def _parse_atomic(self, tokens):
        return AtomicProposition(tokens[0])

    def _parse_not(self, tokens):
        return Not(tokens[0][1])

    def _parse_and(self, tokens):
        return And(tokens[0][0], tokens[0][2])

    def _parse_implies(self, tokens):
        return Implies(tokens[0][0], tokens[0][2])

    def _parse_or(self, tokens):
        return Or(tokens[0][0], tokens[0][2])

    def _parse_until(self, tokens):
        return Until(tokens[0][0], tokens[0][2])

    def _parse_next(self, tokens):
        return Next(tokens[0][1])

    def _parse_prev(self, tokens):
        return Prev(tokens[0][1])

    def _parse_globally(self, tokens):
        return Globally(tokens[0][1])

    def _parse_eventually(self, tokens):
        return Eventually(tokens[0][1])

    def parse(self, expression: str):
        """Parse a string into an LTL formula object."""
        return self.expression.parseString(expression, parseAll=True)[0]
