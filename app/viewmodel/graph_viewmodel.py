from PySide6.QtCore import QObject, Signal

import pm4py
from app.model import EventLog
from pm4py import DcrGraph
from pm4py.visualization.dcr import visualizer as dcr_visualizer


class GraphViewModel(QObject):
    dcr_graph_saved = Signal()

    def __init__(self):
        super().__init__()

    def save_dcr_graph(self, graph: DcrGraph):
        gviz = dcr_visualizer.apply(graph)
        temp_svg_path = "temp_dcr_graph.svg"
        dcr_visualizer.save(gviz, temp_svg_path)
        self.dcr_graph_saved.emit()

    def perform_discovery(self, event_log: EventLog):
        graph, _ = pm4py.discover_dcr(event_log.data)
        self.save_dcr_graph(graph)