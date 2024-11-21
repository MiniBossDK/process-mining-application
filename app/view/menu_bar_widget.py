from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMenuBar, QMessageBox

import pm4py
from app.model.eventlog_list_model import EventLogListModel


class MenuBar(QMenuBar):
    def __init__(self, event_log_model: EventLogListModel):
        super().__init__()
        self.font().setPointSize(18)

        load_action = QAction('Load Event Logs', self)
        load_action.setStatusTip('Load Event Logs')
        load_action.triggered.connect(self.open_file_dialog)
        self.event_log_model = event_log_model
        file_menu = self.addMenu('File')
        file_menu.addAction(load_action)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.handle_file_selected)
        file_dialog.exec()

    def handle_file_selected(self, file_paths):
        for file_path in file_paths:
            try:
                data = pm4py.read_xes(file_path)
                if data.size != 0:
                    QMessageBox.information(self, "Success", "The data has been loaded successfully!")
                    self.event_log_model.event_logs.append(data)
                else:
                    QMessageBox.information(self, "No Data", "No data found in the XES file.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load event log: {str(e)}")