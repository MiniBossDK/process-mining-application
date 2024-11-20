from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class GraphView(QPixmap):
    def __init__(self, file_path: str, width: int, height: int):
        super().__init__()
        self.file_path = file_path
        self.width = width
        self.height = height
        self.scaled(width, height)
        self.fill(Qt.GlobalColor.transparent)

    def render(self):
        pass