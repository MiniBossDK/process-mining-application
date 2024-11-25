from PySide6.QtCore import QObject, Signal, Qt

from app.model import EventLog, EventLogListModel
from app.model.model_list import ModelList


class EventLogListViewModel(QObject):
    selected_event_log_changed = Signal(EventLog)
    event_log_added = Signal(EventLog)

    def __init__(self, event_list_model: EventLogListModel, model_list: ModelList):
        super().__init__()
        self._event_log_model = event_list_model
        self._model_list = model_list
        self._selected_event_log = None

    @property
    def model(self):
        return self._event_log_model

    @property
    def selected_event_log(self):
        return self._selected_event_log

    def set_selected_event_log(self, index):
        if index.isValid():
            self._selected_event_log = self._event_log_model.data(index, Qt.ItemDataRole.UserRole)
            self.selected_event_log_changed.emit(self._selected_event_log)

    def add_event_log(self, eventlog: EventLog):
        self._event_log_model.add_event_log(eventlog)
        self.event_log_added.emit(eventlog)