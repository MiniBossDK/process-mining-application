class EventLogRepository:
    def __init__(self):
        self._event_logs = []
        self.selected_event_log = None

    def add_event_log(self, event_log) -> None:
        self._event_logs.append(event_log)

    def get_all_event_logs(self):
        return self._event_logs

    def set_selected_event_log(self, selected_event_log) -> None:
        self.selected_event_log = selected_event_log