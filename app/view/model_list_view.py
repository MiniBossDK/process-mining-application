from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView, QListWidget, QPushButton, QFileDialog, \
    QMessageBox, QListWidgetItem

import pm4py
from app.model import Model
from app.viewmodel.model_list_viewmodel import ModelListViewModel


class ModelListView(QWidget):

    def __init__(self, viewmodel: ModelListViewModel):
        super().__init__()

        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)

        self.list_label = QLabel("Models")
        self.layout.addWidget(self.list_label)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.model_selected)
        self.viewmodel.model_added.connect(self.on_model_added)

        self.add_button = QPushButton("Add Models")
        self.add_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.add_button)

    def on_model_added(self, model: Model):
        item = QListWidgetItem(model.name)
        item.setData(Qt.ItemDataRole.UserRole, model)
        self.list_widget.addItem(item)

    def add_model(self, model_paths):
        failed_models = []
        for str_path in model_paths:
            path = Path(str_path)
            try:
                model = Model(path.name, self.viewmodel.perform_discovery(path))
            except Exception:
                failed_models.append(path.name)
                continue
            self.viewmodel.add_model(model)
        if len(failed_models) > 0:  (
            QMessageBox.critical(self, "File loading error",
                                 "The following files could not be loaded:\n" + "\n".join(failed_models)))

    def model_selected(self, item: QListWidgetItem):
        self.viewmodel.set_selected_model(item.data(Qt.ItemDataRole.UserRole))

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.add_model)
        file_dialog.exec()