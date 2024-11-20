from typing import List

from PySide6.QtWidgets import QTabWidget

from app.view.eventlog_tab_widget import EventlogTab


class EventlogTabContainer(QTabWidget):
    def __init__(self, tabs: List[EventlogTab]):
        super().__init__()
        self.tabs = tabs
        for tab in tabs:
            self.addTab(tab, tab.name)