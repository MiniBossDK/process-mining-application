# app/view/conformance_checking_view.py
from pathlib import Path

from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QScrollArea, QLabel, QDialog, QHBoxLayout, \
    QTabWidget

from app.model import PetriNetModel
from app.view.alignment_view import AlignmentView
from app.view.tabable_view import TabableView
from app.viewmodel import EventLogListViewModel
from app.viewmodel.conformence_checking_viewmodel import ConformanceCheckingViewModel
from app.viewmodel.model_list_viewmodel import ModelListViewModel


class ConformanceCheckingView(QWidget, TabableView):
    def tab_name(self):
        return 'Conformance Checking'

    def closeable(self):
        return False

    def __init__(self, event_log_list_viewmodel: EventLogListViewModel, model_list_viewmodel: ModelListViewModel, conformance_checking_viewmodel: ConformanceCheckingViewModel ):
        super().__init__()
        self.dialog = None
        self.main_view = None
        self._conformance_checking_viewmodel = conformance_checking_viewmodel
        self._event_log_list_viewmodel = event_log_list_viewmodel
        self._model_list_viewmodel = model_list_viewmodel
        self._error_label = None
        self._error_shown = None
        self.event_log = None
        self.model = None
        self.can_do_conformance_checking = False

        self.layout = QVBoxLayout(self)

        self.conformance_checking_tabs = QTabWidget(self)

        self.layout.addWidget(self.conformance_checking_tabs)

        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.conformance_checking_button = QPushButton('Conformance Checking')

        self.conformance_checking_button.clicked.connect(self.on_conformance_checking_button_clicked)

        self.layout.addWidget(self.conformance_checking_button)

        self._event_log_list_viewmodel.selected_event_log_changed.connect(self.on_event_log_changed)
        self._model_list_viewmodel.selected_petri_net_model_changed.connect(self.on_model_changed)
        self._model_list_viewmodel.selected_dcr_model_changed.connect(self.on_model_changed)
        self._conformance_checking_viewmodel.alignment_image_saved.connect(self.show_alignment)

    def on_event_log_changed(self, event_log):
        self.event_log = event_log
        self.update_conformance_state()

    def on_model_changed(self, model):
        self.model = model
        self.update_conformance_state()

    def update_conformance_state(self):
        self.can_do_conformance_checking = self.event_log is not None and self.model is not None

    def on_conformance_checking_alignment(self):
        if not isinstance(self.model, PetriNetModel) or self.event_log is None:
            QMessageBox.critical(self, 'Conformance Checking Error',
                                 "The selected model must be a PetriNet model.")
            return

        self._conformance_checking_viewmodel.alignment_conformance_checking(self.event_log, self.model)
        self.dialog.close()


    def show_alignment(self, path: Path):
        tab_title = self.event_log.name + " <--> " + self.model.name
        tab = AlignmentView(path)
        index = self.conformance_checking_tabs.addTab(tab, tab_title)
        self.conformance_checking_tabs.tabCloseRequested.connect(lambda: self.conformance_checking_tabs.removeTab(index))
        self.conformance_checking_tabs.setTabsClosable(True)


    def on_conformance_checking_button_clicked(self):

        if not self.can_do_conformance_checking:
            QMessageBox.critical(self, 'Conformance Checking Error',
                                 "Both a model and an event log need to be selected.")
            return

        # Show a message box with options
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Choose Conformance Checking Method")

        vbox = QVBoxLayout()

        self.dialog.setLayout(vbox)

        conformance_checking_method_label = QLabel("Please choose a conformance checking method")

        vbox.addWidget(conformance_checking_method_label)

        hbox = QHBoxLayout()

        alignment_btn = QPushButton("Alignment")

        vbox.addLayout(hbox)
        hbox.addWidget(alignment_btn)

        alignment_btn.clicked.connect(self.on_conformance_checking_alignment)
        self.dialog.exec()