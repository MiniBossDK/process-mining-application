# app/view/conformance_checking_view.py
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox, QScrollArea, QLabel


class ConformanceCheckingView(QWidget):
    def __init__(self, viewmodel, main_view):
        super().__init__()
        self.viewmodel = viewmodel
        self.main_view = main_view

        self.layout = QVBoxLayout(self)

        # Create the button
        self.conformance_checking_button = QPushButton("Conformance checking")
        self.conformance_checking_button.clicked.connect(self.on_conformance_checking_button_clicked)

        # Add the button to the layout
        self.layout.addWidget(self.conformance_checking_button)

        self.update_button_state()

    def update_button_state(self):
        self.conformance_checking_button.setEnabled(self.viewmodel.is_event_log_loaded())

    def on_conformance_checking_button_clicked(self):
        # Show a message box with options
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Choose Conformance Checking Method")
        msg_box.setText("Please choose a conformance checking method:")
        rule_button = msg_box.addButton("Rule Checking", QMessageBox.AcceptRole)
        alignment_button = msg_box.addButton("Alignment Checking", QMessageBox.AcceptRole)
        msg_box.setStandardButtons(QMessageBox.Cancel)
        msg_box.setDefaultButton(QMessageBox.Cancel)
        msg_box.exec()

        if msg_box.result() == QMessageBox.Rejected:
            return

        self.viewmodel.set_active_event_log(self.viewmodel.event_log)
        self.viewmodel.set_active_model_log(self.viewmodel.model_log)

        if msg_box.clickedButton() == rule_button:
            result = self.viewmodel.perform_rule_checking()
            self.main_view.display_result_in_tab(result, "Rule Checking Result")
        elif msg_box.clickedButton() == alignment_button:
            result = self.viewmodel.perform_alignment_checking()
            self.main_view.display_result_in_tab(result, "Alignment Checking Result")

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