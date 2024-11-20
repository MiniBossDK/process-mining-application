from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import QMainWindow, QLabel

from app.view.main_content_widget import MainContentView
from app.view.menu_bar_widget import MenuBar


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        resize_window(self)

        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.setCentralWidget(MainContentView())


def resize_window(self):
    screen = QGuiApplication.primaryScreen().availableGeometry()
    self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))
