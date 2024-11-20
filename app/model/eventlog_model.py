from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from pandas import DataFrame


class EventLog(QAbstractTableModel):
    def __init__(self, eventlog: DataFrame):
        super().__init__()
        self.eventlog = eventlog

    def rowCount(self, parent=QModelIndex()):
        return len(self.eventlog)

    def columnCount(self, parent=QModelIndex()):
        return len(self.eventlog.columns)

    def headerData(self, section, orientation, role = ...):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        return self.eventlog.columns[section]

    def data(self, index, role = ...):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            _, text = self.eventlog[index.row()]
            return text