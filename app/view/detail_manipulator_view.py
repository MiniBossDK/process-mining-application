from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
import sys


class detail_manipulator_view(QWidget):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout()
        self.label = QLabel(message)
        self.button = QPushButton('Roles')
        self.button2 = QPushButton('Pending')
        self.button3 = QPushButton('Timed')

        layout.addWidget(QLabel(title))
        layout.addWidget(self.button)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

        self.setFixedSize(150, 150)




