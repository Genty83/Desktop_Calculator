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
from PySide6.QtCore import Qt, Signal
from typing import List
import qtawesome as qta

from logic.evaluator import ExpressionEvaluator
from ui.buttons import KEYPAD_BUTTONS, SCIENTIFIC_BUTTONS


class CalculatorWidget(QWidget):
    """
    Main calculator interface widget for the desktop application.

    This widget renders the calculator UI, manages layout of all components,
    and handles user interactions such as button clicks and expression evaluation.
    It supports both standard and scientific operations and integrates with
    ExpressionEvaluator for safe mathematical parsing.
    """

    toggle_sidebar = Signal()
    """Signal emitted when the sidebar toggle button is pressed."""

    def __init__(self) -> None:
        """
        Initialize the calculator widget and its components.

        - Instantiates the ExpressionEvaluator for computation.
        - Builds and organizes the UI elements including display field,
            keypad buttons, scientific function buttons, and a floating sidebar toggle.
        """
        super().__init__()
        self.evaluator = ExpressionEvaluator()
        self._init_ui()

    def _init_ui(self) -> None:
        """
        Assemble the UI layout for the calculator.

        This method creates and arranges:
        - A top-aligned 'menu' button for toggling the sidebar.
        - A read-only text display to show and edit mathematical expressions.
        - A grid of standard keypad buttons (digits, basic operators).
        - A grid of scientific calculator buttons (functions, constants).

        Styling and spacing are configured to provide a clean and responsive interface.
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        self.menu_button = QPushButton(self)
        self.menu_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.menu_button.setFixedHeight(40)
        self.menu_button.setStyleSheet("font-size: 16px;")
        self.menu_button.setIcon(qta.icon('fa5s.bars'))
        self.menu_button.clicked.connect(self.toggle_sidebar.emit)
        layout.addWidget(self.menu_button)

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(80)
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(self.display)

        layout.addLayout(self._create_button_grid(KEYPAD_BUTTONS))
        layout.addLayout(self._create_button_grid(SCIENTIFIC_BUTTONS))

    def _create_button_grid(self, button_rows: List[List[str]]) -> QGridLayout:
        """
        Create a grid layout populated with calculator buttons.

        Each button is dynamically generated from the provided 2D list and
        connected to its respective click handler. Buttons are styled to
        expand within their grid cells and maintain consistent spacing.

        Parameters:
        - button_rows (List[List[str]]): Nested list of button labels.

        Returns:
        - QGridLayout: A layout object with fully initialized and connected buttons.
        """
        grid = QGridLayout()
        grid.setSpacing(5)

        for row_index, row in enumerate(button_rows):
            for col_index, label in enumerate(row):
                button = QPushButton(label)
                button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                button.clicked.connect(lambda checked, text=label: self._handle_button_click(text))
                grid.addWidget(button, row_index, col_index)

        return grid

    def _handle_button_click(self, text: str) -> None:
        """
        Handle logic when a calculator button is pressed.

        Depending on the button's label, performs the following:
        - 'C': Clears the display.
        - '=': Evaluates the current expression and displays the result.
        - '^', '√', and scientific functions: Translates input into Python-compatible expressions.
        - All other inputs are appended directly to the expression string.

        Parameters:
        - text (str): The label text of the clicked button.
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
            self.display.setText(self.display.text() + text)