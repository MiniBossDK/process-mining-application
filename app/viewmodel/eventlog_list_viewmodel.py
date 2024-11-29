from pathlib import Path

from PySide6.QtCore import QObject, Signal, Qt

import pm4py
from app.model import EventLog, EventLogRepository
from app.model.repositories.dcr_model_repository import DcrModelRepository


class EventLogListViewModel(QObject):
    selected_event_log_changed = Signal(EventLog)
    event_log_added = Signal(EventLog)

    def __init__(self, event_list_model: EventLogRepository):
        super().__init__()
        self._event_log_model = event_list_model

    def set_selected_event_log(self, event_log: EventLog):
        self._event_log_model.set_selected_event_log(event_log)
        self.selected_event_log_changed.emit(event_log)

    def add_event_log(self, name: str, path: Path, is_selected: bool):
        event_log = EventLog(name, pm4py.read_xes(path.absolute().__str__()), is_selected)
        self._event_log_model.add_event_log(event_log)
        self.event_log_added.emit(event_log)