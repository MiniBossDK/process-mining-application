# main_view.py
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QSplitter, QTabWidget, QMessageBox

from app.model import EventLogRepository, EventLog, Model
from app.model.repositories.model_repository import ModelRepository
from app.view.tabs_view import TabsView
from app.view.alignment_view import AlignmentView
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

        self.event_log_model = EventLogRepository()
        self.model_list = ModelRepository()

        # ViewModels
        self.event_log_list_viewmodel = EventLogListViewModel(self.event_log_model)
        self.Conformance_checking_viewmodel = ConformanceCheckingViewModel(self.event_log_model, self.model_list)
        self.model_list_viewmodel = ModelListViewModel(self.model_list)

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
        self.result_tab_widget = QTabWidget()
        self.result_tab_widget.setTabsClosable(True)
        self.result_tab_widget.tabCloseRequested.connect(self.close_result_tab)
        #self.tab_widget.addTab(self.result_tab_widget, "ConformanceCheckResult")
        splitter.addWidget(self.tab_widget)

        splitter.setSizes([150, 150, 800])



    def resize_window(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))

    def on_event_log_loaded(self, event_log: EventLog):
        self.Conformance_checking_viewmodel.set_event_log_loaded(True, event_log)
        self.conformance_checking_view.update_button_state()

    def on_model_log_loaded(self, model_log: Model):
        self.Conformance_checking_viewmodel.set_model_log_loaded(True, model_log)
        self.conformance_checking_view.update_button_state()

    def display_result_in_tab(self, result_df, title):
        # Check if the tab already exists to prevent duplicates
        for index in range(self.result_tab_widget.count()):
            if self.result_tab_widget.tabText(index) == title:
                self.result_tab_widget.setCurrentIndex(index)
                return

        result_widget = self.Conformance_checking_viewmodel.create_result_widget(result_df)
        self.result_tab_widget.addTab(result_widget, title)
        self.result_tab_widget.setCurrentWidget(result_widget)

    def display_alignment_in_tab(self):
        alignment_view = AlignmentView("alignment_output.svg")
        self.result_tab_widget.addTab(alignment_view, "Alignment Checking Result")
        self.result_tab_widget.setCurrentWidget(alignment_view)

    def close_result_tab(self, index):
        tab_title = self.result_tab_widget.tabText(index)
        if tab_title in ["Rule Checking Result", "Alignment Checking Result"]:
            confirm = QMessageBox.question(
                self,
                "Close Tab",
                f"Are you sure you want to close the '{tab_title}' tab?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )
            if confirm == QMessageBox.StandardButton.Yes:
                self.result_tab_widget.removeTab(index)
        else:
            # Optionally, prevent closing other tabs or handle differently
            QMessageBox.information(
                self,
                "Cannot Close Tab",
                "This tab cannot be closed."
            )
