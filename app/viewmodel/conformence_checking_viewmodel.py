import pm4py
from pm4py import conformance_dcr
import pandas as pd
from pm4py.visualization.petri_net.variants import alignments

from app.model import EventLog


class ConformanceCheckingViewModel:
    def __init__(self):
        self.dcr_graph = None
        self.event_log = None
        self.event_log_loaded = False
        self.active_event_log = None

    def perform_rule_checking(self):
        # Implement the logic for rule-based conformance checking
        result = self.rule_conformance_checking()
        print("Rule-based conformance checking performed")
        return result

    def perform_alignment_checking(self):
        # Implement the logic for alignment-based conformance checking
        result = self.alignment_conformance_checking()
        print("Alignment-based conformance checking performed")
        return result

    def is_event_log_loaded(self):
        return self.event_log_loaded

    def set_event_log_loaded(self, loaded, event_log: EventLog):
        self.event_log_loaded = loaded
        self.event_log = event_log
        self.dcr_graph, _ = pm4py.discover_dcr(self.event_log)

    def set_active_event_log(self, event_log: EventLog):
        self.active_event_log = event_log

    def rule_conformance_checking(self):
        conformance_df = conformance_dcr(self.active_event_log, self.dcr_graph, return_diagnostics_dataframe=True)
        return conformance_df.to_string()

    def alignment_conformance_checking(self):
        # Perform alignment-based conformance checking
        #alignment_sepsis_df = pd.DataFrame(pm4py.optimal_alignment_dcr(self.active_event_log, self.dcr_graph, return_diagnostics_dataframe=True))
        alignment_sepsis_df = pm4py.optimal_alignment_dcr(self.active_event_log, self.dcr_graph, return_diagnostics_dataframe=True)
        return alignment_sepsis_df.to_string()