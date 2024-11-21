from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap

from app.view.zoom_widget import ZoomWidget
from pm4py.visualization.dcr import visualizer as dcr_visualizer
import os


class GraphView(QWidget):
    def __init__(self, file_path: str = "", width: int = 400, height: int = 300):
        super().__init__()
        self.file_path = file_path
        self.layout = QVBoxLayout(self)

        self.zoom_widget = ZoomWidget()
        self.layout.addWidget(self.zoom_widget)

        self.pixmap = QPixmap(self.file_path)
        if not self.pixmap.isNull():
            self.zoom_widget.set_pixmap(self.pixmap)
        else:
            self.zoom_widget.image_label.setText("No Graph Available")

    def update_graph(self, event_log_path: str):
        try:
            import pm4py
            event_log = pm4py.read_xes(event_log_path)
            graph, _ = pm4py.discover_dcr(event_log)

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
            print(f"Error generating the graph: {e}")
            self.zoom_widget.image_label.setText("Error Generating Graph")
