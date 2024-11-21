from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QSplitter, QTabWidget

import pm4py
from app.model.eventlog import EventLog
from app.model.eventlog_list_model import EventLogListModel
from app.model.eventlog_model import EventLogModel
from app.view.event_log_list_view import EventLogListView
from app.view.eventlog_table_view import EventLogDataTableView
from app.view.graph_view import GraphView
from app.viewmodel.eventlog_data_table_viewmodel import EventLogDataTableViewModel
from app.viewmodel.eventlog_list_viewmodel import EventLogListViewModel


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize_window()

        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QHBoxLayout(container)
        splitter = QSplitter()


        main_layout.addWidget(splitter)

        self.layout = QHBoxLayout(container)

        self.event_log_model = EventLogListModel([])


        # ViewModels
        self.event_log_list_viewmodel = EventLogListViewModel(self.event_log_model)
        self.event_log_table_viewmodel = EventLogDataTableViewModel()

        self.event_log_list_viewmodel.selected_event_log_changed.connect(self.event_log_table_viewmodel.on_item_selected)

        self.event_log_list_view = EventLogListView(self.event_log_list_viewmodel)
        splitter.addWidget(self.event_log_list_view)
        self.layout.addWidget(self.event_log_list_view)


        self.event_log_list_view.setMinimumWidth(150)

        self.tab_widget = QTabWidget()
        splitter.addWidget(self.tab_widget)

        self.event_log_table_viewmodel = EventLogDataTableViewModel()
        self.event_log_table_view = EventLogDataTableView(self.event_log_table_viewmodel)

        self.graph_view = GraphView(file_path="", width=400, height=300)

        self.tab_widget.addTab(self.event_log_table_view, "Table")
        self.tab_widget.addTab(self.graph_view, "Graph")

        self.event_log_list_viewmodel.selected_event_log_changed.connect(self.event_log_table_viewmodel.on_item_selected)
        splitter.setSizes([150, 1000])

    def resize_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))
