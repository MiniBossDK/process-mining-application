import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QMessageBox, QScrollArea, QSlider
from PySide6.QtGui import QPixmap, QImageReader, QPainter
from PySide6.QtCore import Qt, QSize
from PySide6.QtSvg import QSvgRenderer
from app.view.menu_bar import MenuBar

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        screen_size = QApplication.primaryScreen().availableGeometry().size()
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.setWindowTitle('Process Miner')

        self.label = QLabel("No Event Log loaded")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.label.font()
        font.setPointSize(100)  # Adjust the font size as needed
        self.label.setFont(font)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setWidgetResizable(True)

        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(500)
        self.zoom_slider.setValue(100)
        self.zoom_slider.valueChanged.connect(self.zoom_image)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.zoom_slider)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setMenuBar(MenuBar(self))
        self.show()

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            QMessageBox.critical(self, "Error", f"File {image_path} does not exist.")
            return

        if image_path.endswith('.svg'):
            renderer = QSvgRenderer(image_path)
            viewBox = renderer.viewBox()
            new_width = viewBox.width()
            new_height = viewBox.height()

            self.pixmap = QPixmap(QSize(new_width, new_height))
            self.pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(self.pixmap)
            renderer.render(painter)
            painter.end()
        else:
            reader = QImageReader(image_path)
            image = reader.read()
            if image.isNull():
                QMessageBox.critical(self, "Error", f"Failed to load image {image_path}.")
                return
            self.pixmap = QPixmap.fromImage(image)
        QMessageBox.information(self, "Success", "The file has been loaded successfully!")
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.pixmap.size())
        self.zoom_slider.setValue(100)

    def zoom_image(self, value):
        if hasattr(self, 'pixmap'):
            scale_factor = value / 100.0
            new_size = self.pixmap.size() * scale_factor
            scaled_pixmap = self.pixmap.scaled(new_size, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.label.setPixmap(scaled_pixmap)
            self.label.resize(scaled_pixmap.size())

def main():
    app = QApplication(sys.argv)
    example = Example()
    app.exec()

if __name__ == '__main__':
    main()