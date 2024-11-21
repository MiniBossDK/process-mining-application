from typing import List

from app.model.eventlog import EventLog


class EventLogModel:
    def __init__(self):
        self._event_logs = []

    def add_event_log(self, event_log: EventLog):
        self._event_logs.append(event_log)

    def get_event_logs(self) -> List[EventLog]:
        return self._event_logs