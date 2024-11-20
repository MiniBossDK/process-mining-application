from PySide6.QtWidgets import QVBoxLayout, QTabWidget, QWidget

from app.view.eventlog_tab_widget import EventlogTab
from app.view.eventlog_tabs_view import EventlogTabContainer


class MainContentView(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox_layout = QVBoxLayout()
        self.setLayout(self.vbox_layout)
        self.tab_widget = EventlogTabContainer([EventlogTab("Hello1", True),
                                                EventlogTab("Hello2", True),
                                                EventlogTab("Hello3", True)])
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.South)
        self.vbox_layout.addWidget(self.tab_widget)