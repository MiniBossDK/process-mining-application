from PySide6.QtCore import QObject, Signal

from app.model.eventlog import EventLog
from app.model.eventlog_model import EventLogModel


class EventLogListViewModel(QObject):
    itemsChanged = Signal()
    itemSelected = Signal(EventLog)


    def __init__(self, model: EventLogModel):
        super().__init__()
        self._model = model

    def get_event_logs(self):
        return self._model.get_event_logs()

    def add_event_log(self, event_log: EventLog):
        self._model.add_event_log(event_log)
        self.itemsChanged.emit()

    def set_selected_event_log(self, event_log: EventLog):
        self.itemSelected.emit(event_log)