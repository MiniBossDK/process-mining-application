from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem

from app.model.eventlog import EventLog
from app.viewmodel.eventlog_data_table_viewmodel import EventLogDataTableViewModel


class EventLogDataTableView(QWidget):
    def __init__(self, viewmodel: EventLogDataTableViewModel):
        super().__init__()
        self.viewmodel = viewmodel

        self.table_view = QTableWidget()

        self.table_view.setEnabled(False)

        viewmodel.itemSelected.connect(self.update_table_data)

    def update_table_data(self, event_log: EventLog):
        '''
        self.table_view.setHorizontalHeaderLabels(event_log.data.keys())
        self.table_view.setColumnCount(len(event_log.data.columns))
        self.table_view.setRowCount(len(event_log.data.index))

        for i, column in enumerate(event_log.data.columns):
            for j, value in enumerate(event_log.data.iloc[:, i]):
                self.table_view.setItem(i, j, QTableWidgetItem(str(value)))

        self.table_view.setEnabled(True)
        '''