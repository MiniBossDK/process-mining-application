import os
import sys

from PySide6.QtSvgWidgets import QGraphicsSvgItem
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget, QMessageBox, QScrollArea, \
    QSlider, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt


from app.view.graph_view import GraphicsView
from app.view.menu_bar import MenuBar

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(1024, 768)
        self.setWindowTitle('Process Miner')


        self.scene = QGraphicsScene()
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.view = GraphicsView(self.zoom_slider, self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.view.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.BoundingRectViewportUpdate)


        self.zoom_in_button = QPushButton("+")
        self.zoom_in_button.clicked.connect(self.zoom_in)

        self.zoom_out_button = QPushButton("-")
        self.zoom_out_button.clicked.connect(self.zoom_out)

        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(500)
        self.zoom_slider.setValue(100)
        self.zoom_slider.valueChanged.connect(self.zoom_image)

        self.zoom_percentage_label = QLabel("100%")


        zoom_layout = QHBoxLayout()
        zoom_layout.addWidget(self.zoom_out_button)
        zoom_layout.addWidget(self.zoom_slider)
        zoom_layout.addWidget(self.zoom_in_button)
        zoom_layout.addWidget(self.zoom_percentage_label)


        layout = QVBoxLayout()
        layout.addLayout(zoom_layout)
        layout.addWidget(self.view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        self.menu_bar = MenuBar(self)
        font = self.menu_bar.font()
        font.setPointSize(12)
        self.menu_bar.setFont(font)
        self.setMenuBar(self.menu_bar)

        self.show()

    def zoom_in(self):
        value = self.zoom_slider.value()
        if value < self.zoom_slider.maximum():
            self.zoom_slider.setValue(value + 10)

    def zoom_out(self):
        value = self.zoom_slider.value()
        if value > self.zoom_slider.minimum():
            self.zoom_slider.setValue(value - 10)

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            QMessageBox.critical(self, "Error", f"File {image_path} does not exist.")
            return

        self.scene.clear()

        if image_path.endswith('.svg'):
            svg_item = QGraphicsSvgItem(image_path)
            self.scene.addItem(svg_item)
            self.current_graphics_item = svg_item
        else:
            pixmap = QPixmap(image_path)
            pixmap_item = QGraphicsPixmapItem(pixmap)
            self.scene.addItem(pixmap_item)
            self.current_graphics_item = pixmap_item


        self.view.fitInView(self.scene.itemsBoundingRect(), Qt.AspectRatioMode.KeepAspectRatio)
        self.zoom_slider.setValue(100)

    def zoom_image(self, value):
        scale_factor = value / 100.0
        self.view.resetTransform()
        self.view.scale(scale_factor, scale_factor)
        self.zoom_percentage_label.setText(f"{value}%")


def main():
    app = QApplication(sys.argv)
    example = Example()
    app.exec()

if __name__ == '__main__':
    main()