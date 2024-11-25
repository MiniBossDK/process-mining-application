from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QListView

from app.viewmodel.model_list_viewmodel import ModelListViewModel


class ModelListView(QWidget):

    def __init__(self, viewmodel: ModelListViewModel):
        super().__init__()

        self.viewmodel = viewmodel

        self.layout = QVBoxLayout(self)

        self.list_label = QLabel("Models")
        self.layout.addWidget(self.list_label)

        self.list_widget = QListView()
        self.layout.addWidget(self.list_widget)

        self.list_widget.setModel(self.viewmodel.model)

        selection_model = self.list_widget.selectionModel().selectionChanged
        selection_model.connect(self.model_selected)

    def model_selected(self, selected, deselected):
        indexes = selected.indexes()
        if indexes:
            self.viewmodel.set_selected_model(indexes[0])