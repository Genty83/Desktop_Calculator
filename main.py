"""
main.py
==============
This is the main entry file to the application.
"""

# Imports
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import QPropertyAnimation, QRect, QEasingCurve

from ui.calculator_widget import CalculatorWidget
from ui.sidebar import Sidebar


class MainWindow(QMainWindow):
    """
    Main application window.

    Initializes and renders the calculator interface and the floating sidebar.
    Handles sidebar animation and layout orchestration.
    """

    def __init__(self):
        """
        Set up the main window with calculator content and floating sidebar.

        - Initializes sidebar as a hidden overlay
        - Sets up central layout with CalculatorWidget
        - Connects sidebar toggle signal from CalculatorWidget
        """
        super().__init__()
        self.setWindowTitle("Desktop Calculator")
        self.setGeometry(100, 100, 300, 500)

        self.initUI()

        self.sidebar = Sidebar(self)
        self.sidebar.setGeometry(0, 0, 0, self.height())
        self.sidebar.raise_()
        self.sidebar.sidebar_close_requested.connect(self.toggle_sidebar)

    def initUI(self):
        """
        Build the main layout and connect calculator signals.

        Adds CalculatorWidget to the main layout and listens for sidebar toggle signal.
        """
        central = QWidget(self)
        layout = QVBoxLayout(central)
        self.setCentralWidget(central)

        self.calculator = CalculatorWidget()
        layout.addWidget(self.calculator)

        # Connect toggle signal from calculator's menu button
        self.calculator.toggle_sidebar.connect(self.toggle_sidebar)

    def resizeEvent(self, event):
        """
        Handle window resize events.

        Ensures sidebar maintains correct height while window dimensions change.
        """
        self.sidebar.setGeometry(0, 0, self.sidebar.width(), self.height())
        super().resizeEvent(event)

    def toggle_sidebar(self):
        """
        Animate the sidebar width to slide it in or out.

        Uses QPropertyAnimation to interpolate sidebar's geometry over time.
        """
        current_width = self.sidebar.width()
        target_width = 200 if current_width == 0 else 0

        animation = QPropertyAnimation(self.sidebar, b"geometry")
        animation.setDuration(1000)
        animation.setStartValue(QRect(0, 0, current_width, self.height()))
        animation.setEndValue(QRect(0, 0, target_width, self.height()))

        # Add easing curve
        animation.setEasingCurve(QEasingCurve.OutCubic)

        animation.start()
        self.sidebar.setFixedWidth(target_width)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
