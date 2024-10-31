import sys

from PySide6.QtWidgets import QMainWindow, QApplication

from app.view.menu_bar import MenuBar

"from app.view.main_window import MainWindow"


class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setMenuBar(MenuBar())

        self.setGeometry(0, 0, self.width(), self.height())
        self.setWindowTitle('Process Miner')
        self.show()


def main():
    app = QApplication(sys.argv)

    window = Example()
    window.show()
    ex = Example()
    app.exec()


if __name__ == '__main__':
    main()