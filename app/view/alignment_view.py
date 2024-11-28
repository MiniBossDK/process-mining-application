import os
from pathlib import Path

from PIL.ImageQt import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout


class AlignmentView(QWidget):
    def __init__(self, file_path: Path):
        super().__init__()
        self.file_path = file_path

        self.layout = QVBoxLayout(self)

        from app.view import ZoomWidget
        self.zoom_widget = ZoomWidget(True, file_path)
        self.zoom_widget.set_path(self.file_path)
        self.layout.addWidget(self.zoom_widget)

        if os.path.exists(file_path):
            os.remove(file_path)