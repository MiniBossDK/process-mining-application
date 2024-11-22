from PySide6.QtCore import QObject, Signal, Qt

from app.model.eventlog import EventLog
from app.model.eventlog_list_model import EventLogListModel


class EventLogListViewModel(QObject):
    selected_event_log_changed = Signal(EventLog)

    def __init__(self, model: EventLogListModel):
        super().__init__()
        self._model = model
        self._selected_event_log = None

    @property
    def model(self):
        return self._model

    @property
    def selected_event_log(self):
        return self._selected_event_log

    def set_selected_event_log(self, index):
        if index.isValid():
            self._selected_event_log = self._model.data(index, Qt.ItemDataRole.UserRole)
            self.selected_event_log_changed.emit(self._selected_event_log)

    def add_event_log(self, eventlog: EventLog):
        self._model.add_event_log(eventlog)