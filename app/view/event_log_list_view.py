from pathlib import Path

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QListView, QMessageBox
from lxml.etree import XMLSyntaxError

import pm4py
from app.model import EventLog
from app.viewmodel import EventLogListViewModel


class EventLogListView(QWidget):

    def __init__(self, viewmodel: EventLogListViewModel):
        super().__init__()

        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)

        self.list_label = QLabel("Event Logs")
        self.layout.addWidget(self.list_label)

        self.list_widget = QListView()
        self.layout.addWidget(self.list_widget)

        self.add_button = QPushButton("Add Event Logs")
        self.add_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.add_button)

        self.list_widget.setModel(self.viewmodel.model)

        selection_model = self.list_widget.selectionModel().selectionChanged
        selection_model.connect(self.event_log_selected)

    def add_event_log(self, event_log_file_paths):
        for str_path in event_log_file_paths:
            path = Path(str_path)
            try:
                event_log = EventLog(path.name, pm4py.read_xes(str_path))
            except XMLSyntaxError:
                QMessageBox.critical(self, "File loading error", "The file " + path.name + " could not be read.")
                continue
            self.viewmodel.add_event_log(event_log)

    def event_log_selected(self, selected, deselected):
        indexes = selected.indexes()
        if indexes:
            self.viewmodel.set_selected_event_log(indexes[0])

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.add_event_log)
        file_dialog.exec()