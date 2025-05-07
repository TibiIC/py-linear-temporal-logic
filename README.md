# py-linear-temporal-logic

A Python library for representing and parsing Linear Temporal Logic (LTL) formulas.

## Features
- Supports atomic propositions, logical operators (AND, OR, NOT), and temporal operators (Globally, Eventually, Until, etc.).
- Includes a parser for converting string formulas into LTL objects.
- MIT licensed.

## Installation
Install the library using pip:
```bash
pip install py-ltl
```

## Usage

```python
from py_ltl.string_parser import LTLStringParser
from py_ltl.formula import LTLFormula

input_formula = "G(p -> X(q U r))"
parser = LTLStringParser()
ltl_formula = LTLFormula.parse(input_formula, parser)
print(ltl_formula)  # Outputs the parsed formula
```