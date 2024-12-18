from enum import Enum
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QFileDialog, \
    QMessageBox, QListWidgetItem, QHBoxLayout, QDialog

from app.model import DcrModel, PetriNetModel
from app.viewmodel.model_list_viewmodel import ModelListViewModel

class ModelListView(QWidget):

    def __init__(self, viewmodel: ModelListViewModel):
        super().__init__()

        self.dialog = None
        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)

        self.list_label = QLabel("Models")
        self.layout.addWidget(self.list_label)

        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.model_selected)
        self.viewmodel.dcr_model_added.connect(self.on_model_added)
        self.viewmodel.petri_net_model_added.connect(self.on_model_added)

        self.list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)

        self.add_button = QPushButton("Add Models")
        self.add_button.clicked.connect(self.open_file_dialog)
        self.layout.addWidget(self.add_button)

    def on_model_added(self, model):
        item = QListWidgetItem(model.name)
        item.setData(Qt.ItemDataRole.UserRole, model)
        item.setText(model.name)
        self.list_widget.addItem(item)

    def add_dcr_model(self, model_paths):
        failed_models = []
        for str_path in model_paths:
            path = Path(str_path)
            try:
                self.viewmodel.add_dcr_model(path)
            except Exception:
                failed_models.append(path.name)
                continue
        if len(failed_models) > 0:  (
            QMessageBox.critical(self, "File loading error",
                                 "The following files could not be loaded:\n" + "\n".join(failed_models)))

    def add_petri_net_model(self, model_paths):
        failed_models = []
        for str_path in model_paths:
            path = Path(str_path)
            try:
                self.viewmodel.add_petri_net_model(path)
            except Exception as e:
                failed_models.append(path.name)
                continue

        if len(failed_models) > 0:  (
            QMessageBox.critical(self, "File loading error",
                                 "The following files could not be loaded:\n" + "\n".join(failed_models)))

    def model_selected(self, item: QListWidgetItem):
        data = item.data(Qt.ItemDataRole.UserRole)

        if isinstance(data, PetriNetModel):
            self.viewmodel.set_selected_petri_net_model(data)
        elif isinstance(data, DcrModel):
            self.viewmodel.set_selected_dcr_model(data)


    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.filesSelected.connect(self.add_petri_net_model)
        file_dialog.exec()