from typing import List

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from app.model.dcr_model import DcrModel


class DcrModelRepository:
    def __init__(self):
        super().__init__()
        self._models = []
        self.selected_model = None

    def add_model(self, model: DcrModel):
        self._models.append(model)

    def get_all_models(self):
        return self._models

    def set_selected_model(self, model: DcrModel):
        self.selected_model = model