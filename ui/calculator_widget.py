from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLineEdit, QGridLayout, QPushButton, QSizePolicy
)
from PySide6.QtCore import Qt
from simpleeval import simple_eval


class CalculatorWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def create_buttons(self):
        grid = QGridLayout()
        grid.setSpacing(5)  # add spacing between buttons

        calculator_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+',
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]
        for position, button_text in zip(positions, calculator_buttons):
            button = QPushButton(button_text)
            # Let buttons expand to fill available space
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(lambda checked, text=button_text: self.on_button_clicked(text))
            grid.addWidget(button, *position)

        return grid

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)  # padding around edges
        layout.setSpacing(10)

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        # Make the display taller and let it expand horizontally only
        self.display.setFixedHeight(80)
        self.display.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.display.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.display)

        buttons_layout = self.create_buttons()
        layout.addLayout(buttons_layout)

    def evaluate_expression(self, expression: str) -> str:
        try:
            result = simple_eval(expression)
            return str(result)
        except Exception:
            return "Error"

    def on_button_clicked(self, text):
        if text == 'C':
            self.display.clear()
        elif text == '=':
            result = self.evaluate_expression(self.display.text())
            self.display.setText(result)
        else:
            current = self.display.text()
            self.display.setText(current + text)
