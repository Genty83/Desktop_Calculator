"""
buttons.py
==============
This module defines the button layout configuration for the calculator UI.

It separates the buttons into two main categories:
- KEYPAD_BUTTONS: The basic numeric and arithmetic keys.
- SCIENTIFIC_BUTTONS: Additional keys for scientific functions and constants.

This structure allows the layout logic in the UI layer to dynamically
generate rows of buttons based on these definitions.

Usage:
    Import KEYPAD_BUTTONS and SCIENTIFIC_BUTTONS into the UI class (e.g., CalculatorWidget)
    to generate the respective rows of buttons.

Example:
    from ui.buttons import KEYPAD_BUTTONS, SCIENTIFIC_BUTTONS
"""

from typing import List

# Standard numeric keypad layout and arithmetic operators
KEYPAD_BUTTONS: List[List[str]] = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
]
"""
KEYPAD_BUTTONS: List[List[str]]
    A list of rows representing standard calculator buttons including digits,
    arithmetic operations, and control buttons ('C', '=').
"""

# Scientific function and constant buttons
SCIENTIFIC_BUTTONS: List[List[str]] = [
    ['sin', 'cos', 'tan', '^'],
    ['log', 'ln', '√', 'e'],
    ['(', ')', 'pi', 'c'],
    ['x!', 'x²', '1/x', 'AC'],
    ['=']
]
"""
SCIENTIFIC_BUTTONS: List[List[str]]
    A list of rows representing scientific calculator functionality.
    Includes trigonometric functions, logarithmic functions, square root,
    parentheses, and mathematical constants.
"""
