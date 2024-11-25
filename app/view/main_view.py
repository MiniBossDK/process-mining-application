from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QSplitter, QTabWidget

from app.model import EventLogListModel, EventLog
from app.model.model_list import ModelList
from app.viewmodel import EventLogListViewModel, EventLogDataTableViewModel
from app.viewmodel.conformence_checking_viewmodel import ConformanceCheckingViewModel
from app.viewmodel.model_list_viewmodel import ModelListViewModel


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
        self.model_list = ModelList([])

        # ViewModels
        self.event_log_list_viewmodel = EventLogListViewModel(self.event_log_model, self.model_list)
        self.event_log_table_viewmodel = EventLogDataTableViewModel()
        self.Conformance_checking_viewmodel = ConformanceCheckingViewModel()
        self.model_list_viewmodel = ModelListViewModel(self.model_list)

        self.event_log_list_viewmodel.selected_event_log_changed.connect(
            self.event_log_table_viewmodel.on_item_selected)
        self.event_log_list_viewmodel.selected_event_log_changed.connect(self.on_event_log_loaded)

        self.event_log_list_viewmodel.event_log_added.connect(self.model_list_viewmodel.add_model)

        self.model_list_viewmodel.selected_model_changed.connect((self.))

        from app.view import EventLogListView
        self.event_log_list_view = EventLogListView(self.event_log_list_viewmodel)
        from app.view import ModelListView
        self.model_list_view = ModelListView(self.model_list_viewmodel)

        splitter.addWidget(self.event_log_list_view)
        splitter.addWidget(self.model_list_view)

        self.layout.addWidget(self.event_log_list_view)
        self.layout.addWidget(self.model_list_view)

        self.event_log_list_view.setMinimumWidth(150)

        self.tab_widget = QTabWidget()
        splitter.addWidget(self.tab_widget)

        from app.view import EventLogDataTableView
        self.event_log_table_view = EventLogDataTableView(self.event_log_table_viewmodel)
        from app.view import GraphView
        self.graph_view = GraphView(file_path="", width=400, height=300)

        self.tab_widget.addTab(self.event_log_table_view, "Table")
        self.tab_widget.addTab(self.graph_view, "Graph")

        self.result_tab_widget = QTabWidget()
        self.tab_widget.addTab(self.result_tab_widget, "Conformance Check Result")

        self.event_log_list_viewmodel.selected_event_log_changed.connect(
            self.event_log_table_viewmodel.on_item_selected)
        self.event_log_list_viewmodel.selected_event_log_changed.connect(self.graph_view.update_graph)

        splitter.setSizes([150, 1000])

        from app.view import ConformanceCheckingView
        self.conformance_checking_view = ConformanceCheckingView(self.Conformance_checking_viewmodel, self)
        main_layout.addWidget(self.conformance_checking_view)

    def resize_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))

    def on_event_log_loaded(self, event_log: EventLog):
        self.Conformance_checking_viewmodel.set_event_log_loaded(True, event_log.data)
        self.Conformance_checking_viewmodel.set_model_log_loaded(True, model_log)
        self.conformance_checking_view.update_button_state()

    def display_result_in_tab(self, result_df, title):
        result_widget = self.Conformance_checking_viewmodel.create_result_widget(result_df)
        self.result_tab_widget.addTab(result_widget, title)
        self.result_tab_widget.setCurrentWidget(result_widget)