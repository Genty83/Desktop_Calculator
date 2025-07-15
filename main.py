""" 
main.py
==============
This is the main entry file to the application.
"""

# Imports
import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from ui.calculator_widget import CalculatorWidget


class MainWindow(QMainWindow): 
    """ 
    MainWindow class that inherits from QMainWindow.
    This class sets up the main window of the application.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Calculator")
        self.setGeometry(100, 100, 300, 500)
        self.initUI()

    def initUI(self):
        """Initialize the user interface components."""
        # Here you can add widgets and layout setup
        self.setCentralWidget(CalculatorWidget())
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())