import os
import sys
from PySide6.QtWidgets import (QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget,
                               QMessageBox, QScrollArea, QSlider, QTableWidget, QTableWidgetItem,
                               QPushButton, QHBoxLayout, QSizePolicy)
from PySide6.QtGui import QPixmap, QImageReader, QPainter
from PySide6.QtCore import Qt, QSize
from PySide6.QtSvg import QSvgRenderer
from app.view.menu_bar import MenuBar

class Example(QMainWindow):

    def _init_(self):
        super(Example, self)._init_()
        self.current_file_path = None
        self.data = None
        self.init_ui()

    def init_ui(self):
        screen_size = QApplication.primaryScreen().availableGeometry().size()
        self.setGeometry(0, 0, screen_size.width(), screen_size.height())
        self.setWindowTitle('Process Miner')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)


        self.zoom_controls_layout = QHBoxLayout()
        self.zoom_controls_widget = QWidget()
        self.zoom_controls_widget.setLayout(self.zoom_controls_layout)
        self.zoom_controls_widget.setVisible(False)

        self.zoom_out_button = QPushButton("-")
        self.zoom_out_button.clicked.connect(self.zoom_out)
        self.zoom_slider = QSlider(Qt.Orientation.Horizontal)
        self.zoom_slider.setMinimum(1)
        self.zoom_slider.setMaximum(500)
        self.zoom_slider.setValue(100)
        self.zoom_slider.valueChanged.connect(self.zoom_image)
        self.zoom_in_button = QPushButton("+")
        self.zoom_in_button.clicked.connect(self.zoom_in)
        self.zoom_label = QLabel("100%")


        self.zoom_slider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)


        self.zoom_controls_layout.addStretch()
        self.zoom_controls_layout.addWidget(self.zoom_out_button)
        self.zoom_controls_layout.addWidget(self.zoom_slider)
        self.zoom_controls_layout.addWidget(self.zoom_in_button)
        self.zoom_controls_layout.addWidget(self.zoom_label)
        self.zoom_controls_layout.addStretch()


        self.main_layout.addWidget(self.zoom_controls_widget)


        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_widget.setLayout(self.content_layout)

        self.label = QLabel("No Event Log loaded")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.label.font()
        font.setPointSize(100)  # Adjust the font size as needed
        self.label.setFont(font)
        self.content_layout.addWidget(self.label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.content_widget)
        self.scroll_area.setWidgetResizable(True)

        self.main_layout.addWidget(self.scroll_area)


        self.bottom_layout = QHBoxLayout()
        self.main_layout.addLayout(self.bottom_layout)

        self.data_button = QPushButton("Data")
        self.graph_button = QPushButton("Graph")

        self.data_button.clicked.connect(self.show_data)
        self.graph_button.clicked.connect(self.show_graph)

        self.bottom_layout.addWidget(self.data_button)
        self.bottom_layout.addWidget(self.graph_button)
        self.bottom_layout.addStretch()

        self.setMenuBar(MenuBar(self))
        self.show()

        self.image_label = None

    def clear_content(self):
        while self.content_layout.count():
            item = self.content_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.zoom_controls_widget.setVisible(False)

        if self.image_label:
            self.image_label.deleteLater()
            self.image_label = None

    def display_data_table(self, data):
        self.clear_content()

        table = QTableWidget()
        table.setRowCount(len(data))

        headers = set()
        for event_data in data:
            headers.update(event_data.keys())
        headers = sorted(headers)

        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        for row, event_data in enumerate(data):
            for col, header in enumerate(headers):
                item = QTableWidgetItem(event_data.get(header, 'N/A'))
                table.setItem(row, col, item)

        self.content_layout.addWidget(table)

    def show_data(self):
        if self.data:
            self.display_data_table(self.data)
        else:
            QMessageBox.information(self, "No Data", "No data to display.")

    def show_graph(self):
        if not self.current_file_path:
            QMessageBox.information(self, "No File", "No file loaded to create a graph.")
            return
        self.create_graph()

    def create_graph(self):
        from app.controller.load_dcr_controller import handle_load
        try:
            handle_load(self.current_file_path)
            self.load_image('output.svg')
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create graph: {str(e)}")

    def load_image(self, image_path):
        self.clear_content()
        if not os.path.exists(image_path):
            QMessageBox.critical(self, "Error", f"File {image_path} does not exist.")
            return

        if image_path.endswith('.svg'):
            renderer = QSvgRenderer(image_path)
            if not renderer.isValid():
                QMessageBox.critical(self, "Error", "Invalid SVG file.")
                return
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

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.resize(self.pixmap.size())

        self.content_layout.addWidget(self.image_label)

        self.zoom_slider.setValue(100)
        self.zoom_controls_widget.setVisible(True)

    def zoom_in(self):
        value = self.zoom_slider.value()
        if value < self.zoom_slider.maximum():
            self.zoom_slider.setValue(value + 10)

    def zoom_out(self):
        value = self.zoom_slider.value()
        if value > self.zoom_slider.minimum():
            self.zoom_slider.setValue(value - 10)
    def zoom_image(self, value):
        if hasattr(self, 'pixmap'):
            scale_factor = value / 100.0
            new_size = self.pixmap.size() * scale_factor
            scaled_pixmap = self.pixmap.scaled(new_size, Qt.AspectRatioMode.KeepAspectRatio,
                                               Qt.TransformationMode.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
            self.image_label.resize(scaled_pixmap.size())
            self.zoom_label.setText(f"{value}%")

def main():
    app = QApplication(sys.argv)
    example = Example()
    app.exec()

if __name__ == '__main__':
    main()