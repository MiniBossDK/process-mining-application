from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class GraphView(QWidget):
    def __init__(self, file_path: str, width: int, height: int):
        super().__init__()
        self.file_path = file_path
        self.width = width
        self.height = height

        self.layout = QVBoxLayout(self)
        self.label = QLabel()
        self.layout.addWidget(self.label)

        pixmap = QPixmap(self.file_path)
        if not pixmap.isNull():
            self.label.setPixmap(pixmap.scaled(self.width, self.height, Qt.KeepAspectRatio))
        else:
            self.label.setText("No Graph Available")

    def render(self):
        pass