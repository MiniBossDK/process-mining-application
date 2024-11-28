# app/view/conformance_checking_view.py
from cProfile import label

from PySide6.QtGui import QGuiApplication, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QScrollArea, QLabel

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
        self.main_view = None
        self.viewmodel = conformance_checking_viewmodel
        self._event_log_list_viewmodel = event_log_list_viewmodel
        self._model_list_viewmodel = model_list_viewmodel
        self._error_label = None
        self._error_shown = None
        self.event_log = None
        self.model = None

        self.layout = QVBoxLayout(self)

        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.conformance_checking_button = QPushButton('Conformance Checking')

        self.conformance_checking_button.clicked.connect(self.on_conformance_checking_button_clicked)

        self.layout.addWidget(self.conformance_checking_button)

        # Create the button
        #self.conformance_checking_button = QPushButton("Conformance checking")
        #self.conformance_checking_button.clicked.connect(self.on_conformance_checking_button_clicked)

        # Add the button to the layout
        #self.layout.addWidget(self.conformance_checking_button)
        #self.layout.addWidget(self.conformance_checking_button)

        #self.show_error_message()

        self._event_log_list_viewmodel.event_log_added.connect(self._on_event_log_changed)
        self._model_list_viewmodel.model_added.connect(self._on_model_changed)

    def _on_event_log_changed(self):
        self.event_log = self._event_log_list_viewmodel.set_selected_event_log
        self._update_error_state()


    def _on_model_changed(self):
        self.model = self._model_list_viewmodel.set_selected_model
        self._update_error_state()

    def _update_error_state(self):
        if self.event_log is None or self.model is None:
            self.show_error_message()
        else:
            self.hide_error_message()

    def show_error_message(self):
        if not self._error_shown:
            if self._error_label is None:
                self._error_label = QLabel("Please choose an event log and a model to do conformance checking")
                self.layout.addWidget(self._error_label)
            self._error_shown = True

    def hide_error_message(self):
        if self._error_shown:  # Only hide if currently shown
            if self._error_label is not None:
                self.layout.removeWidget(self._error_label)
                self._error_label.deleteLater()
                self._error_label = None
            self._error_shown=False

    def update_button_state(self):
        #self.conformance_checking_button.setEnabled(self.viewmodel.is_event_log_loaded())
        pass

    def on_conformance_checking_alignment(self):
        if self.model is None and self.event_log is None:
            self.show_error_message()
        else:
            self.hide_error_message()



    def on_conformance_checking_button_clicked(self):
        # Show a message box with options
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Choose Conformance Checking Method")
        msg_box.setText("Please choose a conformance checking method:")
        rule_button = msg_box.addButton("Rule Checking", QMessageBox.ButtonRole.AcceptRole)
        alignment_button = msg_box.addButton("Alignment Checking", QMessageBox.ButtonRole.AcceptRole)
        #msg_box.setStandardButtons(QMessageBox.StandardButton.Cancel)
        #msg_box.setDefaultButton(QMessageBox.StandardButton.Cancel)
        msg_box.exec()

        if msg_box.result() == QMessageBox.DialogCode.Rejected:
            msg_box.close()
            return

        self.viewmodel.set_active_event_log(self.viewmodel.event_log)
        self.viewmodel.set_active_model_log(self.viewmodel.model_log)

        if msg_box.clickedButton() == rule_button:
            result = self.viewmodel.perform_rule_checking()
            self.main_view.display_result_in_tab(result, "Rule Checking Result")
        elif msg_box.clickedButton() == alignment_button:
            self.viewmodel.perform_alignment_checking()

    def show_result(self, result, title):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)

        scroll_area = QScrollArea(msg_box)
        scroll_area.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_label = QLabel(result)
        content_layout.addWidget(content_label)
        scroll_area.setWidget(content_widget)

        screen = QGuiApplication.primaryScreen().availableGeometry()
        scroll_area.setFixedHeight(screen.height() - 200)
        scroll_area.setFixedWidth(screen.width() // 2)

        msg_box.layout().addWidget(scroll_area)

        msg_box.setMinimumHeight(screen.height() - 200)

        msg_box.setMinimumWidth(screen.width() // 2)

        #msg_box.setText(result)
        msg_box.exec()
