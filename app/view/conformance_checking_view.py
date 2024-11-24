# app/view/conformance_checking_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QMessageBox


class ConformanceCheckingView(QWidget):
    def __init__(self, viewmodel):
        super().__init__()
        self.viewmodel = viewmodel

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
        msg_box.exec()

        if msg_box.clickedButton() == rule_button:
            self.viewmodel.perform_rule_checking()
        elif msg_box.clickedButton() == alignment_button:
            self.viewmodel.perform_alignment_checking()