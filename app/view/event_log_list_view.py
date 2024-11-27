from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QListView, QMessageBox, \
    QListWidget, QListWidgetItem

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

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.add_button = QPushButton("Add Event Logs")
        self.add_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.add_button)

        self.list_widget.itemClicked.connect(self.event_log_selected)
        self.viewmodel.event_log_added.connect(self.on_event_log_add)

        # Make sure the user can only select one item
        self.list_widget.setSelectionMode(QListView.SelectionMode.SingleSelection)

    def on_event_log_add(self, event_log: EventLog):
        item = QListWidgetItem(event_log.name)
        item.setData(Qt.ItemDataRole.UserRole, event_log)
        self.list_widget.addItem(item)

    def add_event_log(self, event_log_file_paths):
        failed_event_logs = []
        for str_path in event_log_file_paths:
            path = Path(str_path)
            try:
                event_log = EventLog(path.name, pm4py.read_xes(str_path), False)
            except Exception:
                continue
            self.viewmodel.add_event_log(event_log)
        if len(failed_event_logs) > 0:  (
            QMessageBox.critical(self, "File loading error", "The following files could not be loaded:\n" + "\n".join(failed_event_logs)))

    def event_log_selected(self, item: QListWidgetItem):
        self.viewmodel.set_selected_event_log(item.data(Qt.ItemDataRole.UserRole))

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.add_event_log)
        file_dialog.exec()