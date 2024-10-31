from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMenuBar

from app.controller.load_dcr_controller import handle_load


class MenuBar(QMenuBar):
    def __init__(self):
        super().__init__()
        load_action = QAction('Load', self)
        load_action.setStatusTip('Load Event Log')
        load_action.triggered.connect(open_file_dialog)

        file_menu = self.addMenu('File')
        file_menu.addAction(load_action)
        self.show()

def open_file_dialog():
    file_dialog = QFileDialog()
    file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
    file_dialog.setNameFilter("All Event Log files (*.xes)")
    file_dialog.fileSelected.connect(handle_load) # TODO - Change this to a more method suitable method
    file_dialog.exec()