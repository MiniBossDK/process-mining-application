from PIL.ImageQt import QPixmap
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import QWidget, QVBoxLayout


class AlignmentView(QWidget):
    def __init__(self, file_path: str):
        super().__init__()
        self.file_path = file_path

        self.layout = QVBoxLayout(self)

        from app.view import ZoomWidget
        self.zoom_widget = ZoomWidget(True)
        self.layout.addWidget(self.zoom_widget)

        self.zoom_widget.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zoom_widget.set_svg(file_path)