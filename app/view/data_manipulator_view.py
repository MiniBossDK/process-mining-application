from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox


class toggleBoxWindow(QWidget):
    toggles_changed = Signal(set)

    def __init__(self):
        super().__init__()

        # Create a box on the right side to hold the toggles

        self.post_process = set()

        toggle_layout = QVBoxLayout(self)

        # Add checkboxes (toggles)
        self.toggle1 = QCheckBox("Timed")
        self.toggle2 = QCheckBox("Roles")
        self.toggle3 = QCheckBox("Pending")

        self.toggle1.stateChanged.connect(self.update_post_process)
        self.toggle2.stateChanged.connect(self.update_post_process)
        self.toggle3.stateChanged.connect(self.update_post_process)

        # Add checkboxes to the box
        toggle_layout.addWidget(self.toggle1)
        toggle_layout.addWidget(self.toggle2)
        toggle_layout.addWidget(self.toggle3)

    def update_post_process(self):
        self.post_process.clear()
        if self.toggle1.isChecked():
            self.post_process.add("timed")
        if self.toggle2.isChecked():
            self.post_process.add("roles")
        if self.toggle3.isChecked():
            self.post_process.add("pending")
        self.toggles_changed.emit(self.post_process)
