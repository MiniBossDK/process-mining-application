from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMenuBar

from app.controller.load_dcr_controller import handle_load


class MenuBar(QMenuBar):
    def __init__(self, example_instance, toggle_window):
        super().__init__()
        self.example_instance = example_instance
        self.toggle_window = toggle_window
        load_action = QAction('Load Event Log', self)
        load_action.setStatusTip('Load Event Log')
        load_action.triggered.connect(self.open_file_dialog)

        file_menu = self.addMenu('File')
        file_menu.addAction(load_action)
        self.show()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.fileSelected.connect(self.handle_file_selected)
        file_dialog.exec()

    def handle_file_selected(self, file_path):
        post_process = self.toggle_window.post_process
        event_log = self.example_instance.data_manipulator.load_event_log(file_path)
        self.example_instance.event_log = event_log
        handle_load(file_path, post_process)
        self.example_instance.load_image('output.svg')
