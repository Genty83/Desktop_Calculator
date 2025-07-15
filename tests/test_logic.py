"""
tests/test_logic.py
===================

Unit tests for the calculator logic modules.

This file tests:

- ExpressionEvaluator class from logic.evaluator
- process_button_input function from logic.utils

Tests cover:
- Basic arithmetic and scientific expression evaluation
- Handling of constants like pi and e
- Graceful handling of invalid expressions
- Correct translation of button clicks to expression strings
"""

import pytest
from logic.evaluator import ExpressionEvaluator
from logic.utils import process_button_input


def test_basic_arithmetic():
    """
    Test that ExpressionEvaluator correctly evaluates basic 
    arithmetic expressions.
    """
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("2 + 3") == "5"
    assert evaluator.evaluate("10 / 2") == "5.0"
    assert evaluator.evaluate("2 * 3 + 4") == "10"


def test_scientific_functions():
    """
    Test that ExpressionEvaluator correctly evaluates 
    expressions with scientific functions.
    """
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("sin(pi / 2)") == "1.0"
    assert evaluator.evaluate("log(100)") == "2.0"
    assert evaluator.evaluate("ln(e)") == "1.0"
    assert evaluator.evaluate("sqrt(16)") == "4.0"
    assert evaluator.evaluate("tan(0)") == "0.0"


def test_constants():
    """
    Test that ExpressionEvaluator correctly recognizes 
    and evaluates mathematical constants.
    """
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("pi") == str(3.141592653589793)
    assert evaluator.evaluate("e") == str(2.718281828459045)


def test_invalid_expression():
    """
    Test that ExpressionEvaluator returns 'Error' 
    for invalid or unsupported expressions.
    """
    evaluator = ExpressionEvaluator()
    assert evaluator.evaluate("2 +") == "Error"
    assert evaluator.evaluate("sqrt(-1)") == "Error"  # math domain error
    assert evaluator.evaluate("unknownFunc(2)") == "Error"


def test_process_button_input():
    """
    Test that the process_button_input function correctly 
    transforms button presses into expression strings.
    """
    # Clear button resets expression
    assert process_button_input("123+4", 'C') == ''

    # '=' button returns expression unchanged (evaluation handled elsewhere)
    assert process_button_input("1+1", '=') == "1+1"

    # Basic character appends
    assert process_button_input("12", "3") == "123"
    assert process_button_input("5+", "+") == "5++"  # No syntax checking here

    # Scientific button translations
    assert process_button_input("2", "^") == "2**"
    assert process_button_input("", "√") == "sqrt("
    assert process_button_input("", "sin") == "sin("
    assert process_button_input("log10", "log") == "log10log("
