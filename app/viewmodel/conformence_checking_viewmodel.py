import pm4py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from pm4py import conformance_dcr, DcrGraph
import pandas as pd
from pm4py.visualization.petri_net.variants import alignments
from app.model import EventLog, Model


class ConformanceCheckingViewModel:
    def __init__(self):
        self.event_dcr_graph = None
        self.model_dcr_graph = None
        self.event_log = None
        self.model_log = None
        self.event_log_loaded = False
        self.model_log_loaded = False
        self.active_event_log = None
        self.active_model_log = None

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

    def is_model_log_loaded(self):
        return self.model_log_loaded

    def set_event_log_loaded(self, loaded, event_log: EventLog):
        self.event_log_loaded = loaded
        self.event_log = event_log
        self.event_dcr_graph, _ = pm4py.discover_dcr(self.event_log)

    def set_model_log_loaded(self, loaded, model_log: DcrGraph):

        self.model_log_loaded = loaded
        self.model_log = model_log

        self.model_dcr_graph = model_log

    def set_active_event_log(self, event_log: EventLog):
        self.active_event_log = event_log

    def set_active_model_log(self, model_log: Model):
        self.active_model_log = model_log

    def rule_conformance_checking(self):
        print(pm4py.discover_dcr(self.active_event_log))
        print()
        print()
        print(self.model_dcr_graph)


        conformance_df = conformance_dcr(self.active_event_log, self.model_dcr_graph,group_key="org:resource", return_diagnostics_dataframe=True)

        print(conformance_df)
        return conformance_df

    def alignment_conformance_checking(self):
        # Perform alignment-based conformance checking
        #alignment_sepsis_df = pd.DataFrame(pm4py.optimal_alignment_dcr(self.active_event_log, self.dcr_graph, return_diagnostics_dataframe=True))
        alignment_sepsis_df = pm4py.optimal_alignment_dcr(self.active_event_log, self.event_dcr_graph,
                                                          return_diagnostics_dataframe=True)
        return alignment_sepsis_df.to_string()

    def create_result_widget(self, result):
        # Create a widget to display the result
        result_widget = QWidget()
        layout = QVBoxLayout(result_widget)

        table_widget = QTableWidget()
        table_widget.setRowCount(result.shape[0])
        table_widget.setColumnCount(result.shape[1])
        table_widget.setHorizontalHeaderLabels(result.columns)

        for i in range(result.shape[0]):
            for j in range(result.shape[1]):
                value = result.iat[i, j]
                if isinstance(value,(int,float)):
                    value = f"{value:.6g}"
                table_widget.setItem(i, j, QTableWidgetItem(str(value)))

        layout.addWidget(table_widget)
        return result_widget

