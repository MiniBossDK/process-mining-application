# main_view.py
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QSplitter

from app.model import EventLogRepository
from app.model.repositories.dcr_model_repository import DcrModelRepository
from app.model.repositories.petrinet_model_repository import PetriNetModelRepository
from app.view.tabs_view import TabsView
from app.viewmodel import EventLogListViewModel
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

        self.event_log_repository = EventLogRepository()
        self.dcr_model_repository = DcrModelRepository()
        self.petri_net_model_repository = PetriNetModelRepository()

        # ViewModels
        self.event_log_list_viewmodel = EventLogListViewModel(self.event_log_repository)
        self.Conformance_checking_viewmodel = ConformanceCheckingViewModel()
        self.model_list_viewmodel = ModelListViewModel(self.dcr_model_repository, self.petri_net_model_repository)

        from app.view import EventLogListView
        self.event_log_list_view = EventLogListView(self.event_log_list_viewmodel)
        from app.view import ModelListView
        self.model_list_view = ModelListView(self.model_list_viewmodel)

        splitter.addWidget(self.event_log_list_view)
        splitter.addWidget(self.model_list_view)

        self.event_log_list_view.setMinimumWidth(150)
        self.model_list_view.setMinimumWidth(150)

        from app.view import EventLogDataTableView
        self.event_log_table_view = EventLogDataTableView(self.event_log_list_viewmodel)
        from app.view import GraphView
        self.graph_view = GraphView(self.event_log_list_viewmodel)
        from app.view import ConformanceCheckingView
        self.conformance_checking_view = ConformanceCheckingView(self.event_log_list_viewmodel,
                                                                 self.model_list_viewmodel,self.Conformance_checking_viewmodel)

        self.tab_widget = TabsView([self.event_log_table_view, self.graph_view, self.conformance_checking_view])
        splitter.addWidget(self.tab_widget)

        splitter.setSizes([150, 150, 800])



    def resize_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))