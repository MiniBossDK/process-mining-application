from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget

import pm4py
from app.model.eventlog import EventLog
from app.model.eventlog_model import EventLogModel
from app.view.event_log_list_view import EventLogListView
from app.view.eventlog_table_view import EventLogDataTableView
from app.viewmodel.eventlog_data_table_viewmodel import EventLogDataTableViewModel
from app.viewmodel.eventlog_list_viewmodel import EventLogListViewModel


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        resize_window(self)

        container = QWidget()

        self.layout = QHBoxLayout(container)

        self.event_log_model = EventLogModel()
        self.event_log_model.add_event_log(EventLog("Hello1"))
        self.event_log_model.add_event_log(EventLog("Hello2"))
        self.event_log_model.add_event_log(EventLog("Hello3"))
        self.event_log_model.add_event_log(EventLog("Hello4"))

        self.event_log_list_viewmodel = EventLogListViewModel(self.event_log_model)
        self.event_log_table_viewmodel = EventLogDataTableViewModel()

        self.event_log_list_viewmodel.itemSelected.connect(self.event_log_table_viewmodel.on_item_selected)

        self.event_log_list_view = EventLogListView(self.event_log_list_viewmodel)

        self.layout.addWidget(self.event_log_list_view)

        self.setCentralWidget(container)


def resize_window(self):
    screen = QGuiApplication.primaryScreen().availableGeometry()
    self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))
