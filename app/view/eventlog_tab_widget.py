from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget, QPushButton, QWidget


class EventlogTab(QTabWidget):
    def __init__(self, name: str, is_selected: bool):
        super().__init__()
        self.is_selected = is_selected
        self.name = name
        self.setTabShape(QTabWidget.TabShape.Rounded)
        self.graph_tab = QTabWidget(self)
        self.event_log_tab = QTabWidget(self)

        self.addTab(self.graph_tab, "Data")
        self.addTab(self.event_log_tab, "Graph")
        self.setTabPosition(QTabWidget.TabPosition.South)