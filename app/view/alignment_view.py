import os
from pathlib import Path

from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy


class AlignmentView(QWidget):
    def __init__(self, file_path: Path):
        super().__init__()
        self.file_path = file_path

        self.layout = QVBoxLayout(self)

        self.svg_widget = QSvgWidget(self)
        self.svg_widget.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.layout.addWidget(self.svg_widget)
        self.svg_widget.load(file_path.absolute().__str__())

        if os.path.exists(file_path):
            os.remove(file_path)