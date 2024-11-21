from typing import List

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from app.model.eventlog import EventLog


class EventLogListModel(QAbstractListModel):
    def __init__(self, event_logs: List[EventLog]):
        super().__init__()
        self._event_logs = event_logs

    def data(self, index, role = ...):
        event_log = self._event_logs[index.row()]  # Get the object for the row
        if role == Qt.ItemDataRole.DisplayRole:
            return event_log.name
        if role == Qt.ItemDataRole.UserRole:
            return event_log

    def rowCount(self, parent= ...):
        return len(self._event_logs)

    def add_event_log(self, event_log: EventLog):
        self.beginInsertRows(QModelIndex(), len(self._event_logs), len(self._event_logs))
        self._event_logs.append(event_log)
        self.endInsertRows()