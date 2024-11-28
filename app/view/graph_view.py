import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QVBoxLayout

import pm4py
from app.model import EventLog
from app.view import ZoomWidget
from app.view.tabable_view import TabableView
from app.viewmodel import EventLogListViewModel
from pm4py.visualization.dcr import visualizer as dcr_visualizer


class GraphView(QWidget, TabableView):

    def closeable(self):
        return False

    def tab_name(self):
        return "Graph"

    def __init__(self, event_log_list_viewmodel: EventLogListViewModel):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self._event_log_list_viewmodel = event_log_list_viewmodel

        self.temp_svg_path = "temp_dcr_graph.svg"

        self.zoom_widget = ZoomWidget(False, Path(self.temp_svg_path))
        self.layout.addWidget(self.zoom_widget)

        self.zoom_widget.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._event_log_list_viewmodel.selected_event_log_changed.connect(self.update_graph)

        self.zoom_widget.image_label.setText("No Graph Available")

    def update_graph(self, event_log: EventLog):
        try:
            graph, _ = pm4py.discover_dcr(event_log.data)

            gviz = dcr_visualizer.apply(graph)

            temp_svg_path = "temp_dcr_graph.svg"
            dcr_visualizer.save(gviz, temp_svg_path)

            pixmap = QPixmap(temp_svg_path)
            pixmap.scaled(self.size())
            if not pixmap.isNull():
                self.zoom_widget.set_pixmap(pixmap)
            else:
                self.zoom_widget.image_label.setText("Unable to Render Graph")

            if os.path.exists(temp_svg_path):
                os.remove(temp_svg_path)
        except Exception as e:
            self.zoom_widget.image_label.setText("Error Generating Graph")