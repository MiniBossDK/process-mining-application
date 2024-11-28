from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSlider, QLabel,
    QSizePolicy, QScrollArea
)


class ZoomWidget(QWidget):
    def __init__(self, is_svg: bool, path: Path):
        super().__init__()
        self.zoom_slider = None
        self.is_svg = is_svg
        self.path = path
        self.pixmap: QPixmap = None
        self.image_label = QLabel()
        self.svg_widget = None
        self.min_zoom = 10
        self.max_zoom = 300
        self.zoom_step = 10
        self.default_zoom = 100
        self.svg_width = None
        self.svg_height = None
        self.init_ui()

    def init_ui(self):
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        self.image_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.image_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

        self.zoom_out_button = QPushButton("-")
        self.zoom_in_button = QPushButton("+")
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_label = QLabel(f"{self.default_zoom}%")

        if self.is_svg:
            self.svg_widget = QSvgWidget(self)
            self.svg_widget.renderer().setAspectRatioMode(Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            self.scroll_area.setWidget(self.svg_widget)
            self.svg_widget.setMinimumWidth(self.svg_widget.height() * 3)
            self.set_svg()
            self.svg_width = self.svg_widget.width()
            self.svg_height = self.svg_widget.height()
        else:
            self.set_pixmap(QPixmap(self.path.absolute().__str__()))
            self.scroll_area.setWidget(self.image_label)

        self.main_layout.addWidget(self.scroll_area)

        self.zoom_controls_layout = QHBoxLayout()
        self.zoom_controls_layout.setContentsMargins(0, 5, 0, 0)
        self.zoom_controls_layout.setSpacing(5)

        self.zoom_slider.setMinimum(self.min_zoom)
        self.zoom_slider.setMaximum(self.max_zoom)
        self.zoom_slider.setValue(self.default_zoom)
        self.zoom_slider.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self.zoom_controls_layout.addStretch()
        self.zoom_controls_layout.addWidget(self.zoom_out_button)
        self.zoom_controls_layout.addWidget(self.zoom_slider)
        self.zoom_controls_layout.addWidget(self.zoom_in_button)
        self.zoom_controls_layout.addWidget(self.zoom_label)
        self.zoom_controls_layout.addStretch()

        self.main_layout.addLayout(self.zoom_controls_layout)

        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_slider.valueChanged.connect(self.zoom_image)

    def set_pixmap(self, pixmap):
        self.pixmap = pixmap
        self.zoom_image(self.zoom_slider.value())

    def set_svg(self):
        self.svg_widget.load("alignment_output.svg")

    def zoom_in(self):
        value = min(self.zoom_slider.value() + self.zoom_step, self.max_zoom)
        self.zoom_slider.setValue(value)

    def zoom_out(self):
        value = max(self.zoom_slider.value() - self.zoom_step, self.min_zoom)
        self.zoom_slider.setValue(value)

    def zoom_image(self, value):
        scale_factor = value / 100.0
        if self.svg_widget:
            self.svg_widget.setFixedSize(self.svg_width * scale_factor, self.svg_height * scale_factor)

        if self.pixmap:
            new_size = self.pixmap.size() * scale_factor
            scaled_pixmap = self.pixmap.scaled(
                new_size,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(scaled_pixmap)
            self.zoom_label.setText(f"{value}%")
            self.image_label.adjustSize()

    def set_path(self, file_path):
        self.path = file_path