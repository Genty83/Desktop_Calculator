"""
calculator_widget.py
====================
This module defines the CalculatorWidget class, responsible for rendering
the calculator interface and handling user interaction.

The widget supports both basic keypad buttons and scientific calculator
buttons. It uses the ExpressionEvaluator class to safely evaluate
mathematical expressions input by the user.

Features:
- Numeric keypad and basic arithmetic operators
- Scientific functions such as sin, cos, tan, log, ln, sqrt, pi, and e
- Expression evaluation with error handling
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt
from typing import List

from logic.evaluator import ExpressionEvaluator
from ui.buttons import KEYPAD_BUTTONS, SCIENTIFIC_BUTTONS


class CalculatorWidget(QWidget):
    """
    CalculatorWidget handles the UI and interaction logic for a calculator,
    including both basic keypad and scientific function buttons.

    The widget displays the current expression in a read-only QLineEdit
    and updates the expression based on user button clicks.

    When the '=' button is clicked, the expression is evaluated and the
    result is displayed. Errors during evaluation display "Error".
    """

    def __init__(self) -> None:
        """
        Initialize the CalculatorWidget.

        Sets up the ExpressionEvaluator and builds the UI components.
        """
        super().__init__()
        self.evaluator = ExpressionEvaluator()
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Initialize and assemble the UI layout.

        Creates a vertical layout containing:
        - A display line edit for expression and results
        - A grid layout for basic keypad buttons
        - A grid layout for scientific function buttons
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.display)

        # Add basic keypad buttons
        layout.addLayout(self._create_button_grid(KEYPAD_BUTTONS))

        # Add scientific buttons below the keypad
        layout.addLayout(self._create_button_grid(SCIENTIFIC_BUTTONS))

    def _create_button_grid(self, button_rows: List[List[str]]) -> QGridLayout:
        """
        Generate a grid layout of calculator buttons from a list of rows.

        Each string in the rows corresponds to a button label. Buttons
        will be added in a grid matching the row/column structure.

        :param button_rows: List of rows of button labels.
        :return: QGridLayout with buttons arranged and signals connected.
        """
        grid = QGridLayout()
        grid.setSpacing(5)

        for row_index, row in enumerate(button_rows):
            for col_index, label in enumerate(row):
                button = QPushButton(label)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                # Use lambda default arg to capture current label correctly
                button.clicked.connect(lambda checked, text=label: self._handle_button_click(text))
                grid.addWidget(button, row_index, col_index)

        return grid

    def _handle_button_click(self, text: str) -> None:
        """
        Handle a button click event based on the button's label.

        - 'C' clears the display.
        - '=' evaluates the expression and shows the result or "Error".
        - '^' is translated to Python exponent operator '**'.
        - '√' is translated to 'sqrt(' to begin square root function.
        - Scientific function buttons like 'sin', 'cos', 'tan', 'log', 'ln'
            append the function name followed by an opening parenthesis '('.
        - Other buttons append their label text directly to the display.

        :param text: The label of the button clicked.
        """
        if text == 'C':
            self.display.clear()
        elif text == '=':
            result = self.evaluator.evaluate(self.display.text())
            self.display.setText(result)
        else:
            if text == '^':
                text = '**'
            elif text == '√':
                text = 'sqrt('
            elif text in ('sin', 'cos', 'tan', 'log', 'ln'):
                text += '('
            # Append button text or translated equivalent to the display
            self.display.setText(self.display.text() + text)
