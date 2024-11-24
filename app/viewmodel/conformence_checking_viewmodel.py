import pm4py
from pm4py import conformance_dcr
import pandas as pd

from app.model import EventLog


class ConformanceCheckingViewModel:
    def __init__(self):
        self.dcr_graph = None
        self.event_log = None
        self.event_log_loaded = False

    def perform_rule_checking(self):
        # Implement the logic for rule-based conformance checking
        result = self.rule_conformance_checking()
        print("Rule-based conformance checking performed")
        return result

    def perform_alignment_checking(self):
        # Implement the logic for alignment-based conformance checking
        print("Alignment-based conformance checking performed")

    def is_event_log_loaded(self):
        return self.event_log_loaded

    def set_event_log_loaded(self, loaded, event_log: EventLog):
        self.event_log_loaded = loaded
        self.event_log = event_log

        self.dcr_graph, _ = pm4py.discover_dcr(self.event_log)

    def rule_conformance_checking(self):
        conformance_df = pd.DataFrame(conformance_dcr(self.event_log, self.dcr_graph))
        return conformance_df.to_string()
