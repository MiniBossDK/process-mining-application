from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

from app.model.eventlog import EventLog
from app.viewmodel.eventlog_data_table_viewmodel import EventLogDataTableViewModel

class EventLogDataTableView(QWidget):
    def __init__(self, viewmodel: EventLogDataTableViewModel):
        super().__init__()
        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)
        self.table_view = QTableWidget()
        self.layout.addWidget(self.table_view)

        self.table_view.setEnabled(False)

        self.viewmodel.itemSelected.connect(self.update_table_data)

    def update_table_data(self, event_log: EventLog):
        self.table_view.setColumnCount(len(event_log.data.columns))
        self.table_view.setRowCount(len(event_log.data.index))
        self.table_view.setHorizontalHeaderLabels(event_log.data.columns)

        for row_idx, row in event_log.data.iterrows():
            for col_idx, value in enumerate(row):
                self.table_view.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        self.table_view.setEnabled(True)
