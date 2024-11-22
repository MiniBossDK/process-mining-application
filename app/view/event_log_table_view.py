import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QTableView

from app.model import EventLog
from app.viewmodel import EventLogDataTableViewModel


class EventLogDataTableView(QWidget):
    def __init__(self, viewmodel: EventLogDataTableViewModel):
        super().__init__()
        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)
        self.table_view = QTableWidget()
        # Disable for now until edit implementation is done
        self.table_view.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

        self.layout.addWidget(self.table_view)

        self.viewmodel.itemSelected.connect(self.update_table_data)

    def update_table_data(self, event_log: EventLog):
        self.table_view.setColumnCount(len(event_log.data.columns))
        self.table_view.setRowCount(len(event_log.data.index))
        self.table_view.setHorizontalHeaderLabels(event_log.data.columns)

        for i, row in enumerate(event_log.data.to_numpy()):
            for j, value in enumerate(row):
                if pd.isna(value) or pd.isnull(value):
                    continue
                self.table_view.setItem(i, j, QTableWidgetItem(str(value)))