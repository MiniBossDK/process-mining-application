from PySide6.QtCore import Signal, QObject

from app.model.eventlog import EventLog


class EventLogDataTableViewModel(QObject):
    itemSelected = Signal(EventLog)

    def __init__(self):
        super().__init__()

    def on_item_selected(self, eventlog: EventLog):
        self.itemSelected.emit(eventlog)

