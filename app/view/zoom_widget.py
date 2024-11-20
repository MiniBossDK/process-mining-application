from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSlider, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

class ZoomWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap = None
        self.image_label = None
        self.init_ui()

    def init_ui(self):
        self.zoom_controls_layout = QHBoxLayout(self)
        self.zoom_controls_layout.addStretch()

        self.zoom_out_button = QPushButton("-")
        self.zoom_in_button = QPushButton("+")
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_label = QLabel("100%")

        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(500)
        self.zoom_slider.setValue(100)
        self.zoom_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.zoom_controls_layout.addWidget(self.zoom_out_button)
        self.zoom_controls_layout.addWidget(self.zoom_slider)
        self.zoom_controls_layout.addWidget(self.zoom_in_button)
        self.zoom_controls_layout.addWidget(self.zoom_label)
        self.zoom_controls_layout.addStretch()

        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_slider.valueChanged.connect(self.zoom_image)

    def set_pixmap(self, pixmap):
        self.pixmap = pixmap

    def set_image_label(self, image_label):
        self.image_label = image_label

    def zoom_in(self):
        value = self.zoom_slider.value()
        if value < self.zoom_slider.maximum():
            self.zoom_slider.setValue(value + 10)

    def zoom_out(self):
        value = self.zoom_slider.value()
        if value > self.zoom_slider.minimum():
            self.zoom_slider.setValue(value - 10)

    def zoom_image(self, value):
        if self.pixmap and self.image_label:
            scale_factor = value / 100.0
            new_size = self.pixmap.size() * scale_factor
            scaled_pixmap = self.pixmap.scaled(
                new_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.resize(scaled_pixmap.size())
            self.zoom_label.setText(f"{value}%")
