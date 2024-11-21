from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap

from app.view.zoom_widget import ZoomWidget

class GraphView(QWidget):
    def __init__(self, file_path: str = "", width: int = 400, height: int = 300):
        super().__init__()
        self.file_path = file_path

        self.layout = QVBoxLayout(self)

        # Initialize ZoomWidget
        self.zoom_widget = ZoomWidget()
        self.layout.addWidget(self.zoom_widget)

        # Load the pixmap
        self.pixmap = QPixmap(self.file_path)
        if not self.pixmap.isNull():
            self.zoom_widget.set_pixmap(self.pixmap)
        else:
            self.zoom_widget.image_label.setText("No Graph Available")

    def render(self):
        # Implement rendering logic if needed
        pass
