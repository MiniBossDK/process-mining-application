from typing import List

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from app.model import EventLog


class EventLogRepository:
    def __init__(self):
        self._event_logs = []
        self.selected_event_log = None


    def add_event_log(self, event_log: EventLog) -> None:
        self._event_logs.append(event_log)

    def get_all_event_logs(self) -> List[EventLog]:
        return self._event_logs

    def set_selected_event_log(self, selected_event_log: EventLog) -> None:
        self.selected_event_log = selected_event_log