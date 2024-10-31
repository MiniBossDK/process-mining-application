import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QMessageBox, QScrollArea
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

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)

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

            pixmap = QPixmap(QSize(new_width, new_height))
            pixmap.fill(Qt.GlobalColor.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
        else:
            reader = QImageReader(image_path)
            image = reader.read()
            if image.isNull():
                QMessageBox.critical(self, "Error", f"Failed to load image {image_path}.")
                return
            pixmap = QPixmap.fromImage(image)

        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.size())

def main():
    app = QApplication(sys.argv)
    example = Example()
    app.exec()

if __name__ == '__main__':
    main()