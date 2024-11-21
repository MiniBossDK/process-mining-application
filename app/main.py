import sys

from PySide6.QtWidgets import (
    QApplication
)

from app.view.main_view import MainView


def main():
    app = QApplication(sys.argv)
    main_view = MainView()
    main_view.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
