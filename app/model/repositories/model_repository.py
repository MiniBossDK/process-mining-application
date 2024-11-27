from typing import List

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from app.model.model import Model


class ModelRepository:
    def __init__(self):
        super().__init__()
        self._models = []
        self.selected_model = None

    def add_model(self, model: Model):
        self._models.append(model)

    def get_all_models(self):
        return self._models

    def set_selected_model(self, model: Model):
        self.selected_model = model