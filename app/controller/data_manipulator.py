import pm4py


class DataManipulator():
    def __init__(self):
        self.event_log = None

    def load_event_log(self, path: str):
        self.event_log = pm4py.read_xes(path)
        return self.event_log

    def discover_dcr_with_post_process(self, event_log, *post_process):
        if self.event_log is None:
            raise ValueError("Event log not loaded. Please load the event log first.")
        post_process_set = set(post_process) if post_process else None
        return pm4py.discover_dcr(event_log, post_process=post_process_set, group_key="org:resource")



