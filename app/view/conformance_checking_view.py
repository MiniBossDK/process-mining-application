# app/view/conformance_checking_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

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

    def on_conformance_checking_button_clicked(self):
        # Handle the button click event
        self.viewmodel.perform_conformance_checking()