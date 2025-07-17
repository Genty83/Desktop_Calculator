""" 
sidebar.py
==========================

"""

# Import
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout, QPushButton
from PySide6.QtCore import Signal, Qt

class Sidebar(QWidget):
    sidebar_close_requested = Signal()  # New signal

    def __init__(self, parent=None):
        super(Sidebar, self).__init__(parent)
        self.setObjectName("sidebar")
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            #sidebar {
                background-color: hsl(0, 10%, 10%);
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        close_button = QPushButton("Close Sidebar")
        close_button.setFixedHeight(40)
        layout.addWidget(close_button)

        close_button.clicked.connect(self.sidebar_close_requested.emit)