import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QTableView

from app.model import EventLog
from app.view.tabable_view import TabableView
from app.viewmodel import EventLogListViewModel


class EventLogDataTableView(QWidget, TabableView):
    def closeable(self):
        return False

    def tab_name(self):
        return "Table"

    def __init__(self, viewmodel: EventLogListViewModel):
        super().__init__()
        self.viewmodel = viewmodel

        self.is_selected = False

        self.layout = QVBoxLayout(self)
        self.table_view = QTableWidget()
        self.table_view.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)
        self.label = QLabel("No event log selected")
        if self.is_selected:
            self.show_table_data()
        else:
            self.show_error_message()

        self.viewmodel.selected_event_log_changed.connect(self.update_table_data)

    def show_table_data(self):
        self.layout.removeWidget(self.label)
        self.layout.addWidget(self.table_view)

    def show_error_message(self):
        self.layout.removeWidget(self.table_view)
        self.layout.addWidget(self.label)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def update_table_data(self, event_log: EventLog):
        self.table_view.setColumnCount(len(event_log.data.columns))
        self.table_view.setRowCount(len(event_log.data.index))
        self.table_view.setHorizontalHeaderLabels(event_log.data.columns)

        for i, row in enumerate(event_log.data.to_numpy()):
            for j, value in enumerate(row):
                if pd.isna(value) or pd.isnull(value):
                    continue
                self.table_view.setItem(i, j, QTableWidgetItem(str(value)))

        self.show_table_data()