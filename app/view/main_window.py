import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QVBoxLayout, QWidget, QMenuBar
from PySide6.QtGui import QAction
from app.controller.graph import load

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DCR Graph Viewer")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.create_menu()

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        load_action = QAction("Load DCR Graph", self)
        load_action.triggered.connect(self.load_graph)
        file_menu.addAction(load_action)

    def load_graph(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open XES File", "", "XES Files (*.xes)")
        if file_path:
            print(f"Selected file: {file_path}")
            load([file_path])

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec()