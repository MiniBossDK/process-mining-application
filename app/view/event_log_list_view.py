from pathlib import Path

from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QLabel, QFileDialog, QListWidgetItem

from app.model.eventlog import EventLog
from app.viewmodel.eventlog_list_viewmodel import EventLogListViewModel


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

        self.viewmodel.itemsChanged.connect(self.update_list)
        self.update_list()

    def update_list(self):
        self.list_widget.clear()
        for eventlog in self.viewmodel.get_event_logs():
            self.list_widget.addItem(eventlog.name)

    def add_event_log(self, event_log_file_paths):
        for str_path in event_log_file_paths:
            path = Path(str_path)
            event_log= EventLog(path.name)
            self.viewmodel.add_event_log(event_log)

    def event_log_selected(self, item: QListWidgetItem):
        print(item.text())

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.add_event_log)
        file_dialog.exec()