import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from app.view.main_window import MainWindow


"""
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test")
        button = QPushButton("Click me")

        self.setFixedSize(400, 300)

        self.setCentralWidget(button)
"""

app = QApplication([])

window = MainWindow()
window.show()
app.exec()
