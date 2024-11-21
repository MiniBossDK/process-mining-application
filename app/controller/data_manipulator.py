import pm4py
from pm4py.visualization.dcr import visualizer as dcr_visualizer
import os

from app.controller.load_dcr_controller import save_gviz_as_svg


class DataManipulator:
    def __init__(self):
        self.event_log = None

    def load_event_log(self, path: str):
        self.event_log = pm4py.read_xes(path)
        return self.event_log


