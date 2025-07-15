"""
evaluator.py
==============
This module defines an ExpressionEvaluator class responsible for safely
evaluating mathematical expressions using the `simpleeval` library.

Features:
- Supports basic and scientific operators
- Safely evaluates strings like "2 + sin(pi / 2)"
- Easily extendable with new functions or constants

Dependencies:
- simpleeval
- math
"""

from simpleeval import simple_eval, DEFAULT_FUNCTIONS
import math
from typing import Dict, Callable, Any


class ExpressionEvaluator:
    """
    ExpressionEvaluator provides a clean interface for evaluating
    mathematical expressions using a predefined set of safe functions and constants.
    """

    def __init__(
        self,
        functions: Dict[str, Callable] = None,
        constants: Dict[str, Any] = None
    ):
        """
        Initialize the evaluator with optional custom functions and constants.

        :param functions: Dictionary of allowed functions (e.g., {'sin': math.sin})
        :param constants: Dictionary of allowed constants (e.g., {'pi': math.pi})
        """
        self.functions = {
            **DEFAULT_FUNCTIONS,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            '√': math.sqrt,
            **(functions or {})
        }

        self.constants = {
            'pi': math.pi,
            'e': math.e,
            **(constants or {})
        }

    def evaluate(self, expression: str) -> str:
        """
        Evaluate the given mathematical expression as a string.

        :param expression: A string containing the expression to evaluate.
        :return: The result as a string, or "Error" if evaluation fails.
        """
        try:
            result = simple_eval(
                expression,
                functions=self.functions,
                names=self.constants
            )
            return str(result)
        except Exception:
            return "Error"
