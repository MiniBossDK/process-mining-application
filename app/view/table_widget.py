from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

from app.model.eventlog import EventLog


class EventlogTableWidget(QTableWidget):
    def __init__(self, eventlog: EventLog):
        super().__init__()
        self.eventlog = eventlog
        self.setColumnCount(eventlog.data.columns.size)
        self.setRowCount(eventlog.data.rows.size)
        for row in range(eventlog.data.rows.size):
            for col in range(eventlog.data.columns.size):
                self.setItem(row, col, QTableWidgetItem(str(eventlog.data.columns[col])))
        self.setHorizontalHeaderLabels(eventlog.data.columns.keys())