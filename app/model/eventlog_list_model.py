from typing import List

from PySide6.QtCore import QAbstractListModel, Qt

from pm4py.objects.log.obj import EventLog


class EventLogListModel(QAbstractListModel):
    def __init__(self, event_logs: List[EventLog]):
        super().__init__()
        self.event_logs = event_logs

    def data(self, index, role = ...):
        if role == Qt.ItemDataRole.DisplayRole:
            event_log = self.event_logs[index.row()]
            return event_log

    def rowCount(self, parent= ...):
        return len(self.event_logs)
