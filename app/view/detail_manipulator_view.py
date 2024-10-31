from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
import sys


class detail_manipulator_view(QWidget):
    def __init__(self, title, message, color, parent=None):
        super().__init__(parent)


        layout = QVBoxLayout()
        self.label = QLabel(message)
        self.button = QPushButton('Test button')

        layout.addWidget(QLabel(title))
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)



