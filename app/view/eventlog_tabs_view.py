from typing import List

from PySide6.QtWidgets import QTabWidget, QLabel

from app.view.eventlog_tab_widget import EventlogTab


class EventlogTabContainer(QTabWidget):
    def __init__(self, tabs: List[EventlogTab]):
        super().__init__()
        self.setVisible(True)
        if tabs is None:
            tabs = []

        if len(tabs) == 0:
            self.setVisible(False)

        self.tabs = tabs
        for tab in tabs:
            self.addTab(tab, tab.name)