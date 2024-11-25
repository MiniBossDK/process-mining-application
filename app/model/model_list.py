from typing import List

from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex

from app.model.model import Model


class ModelList(QAbstractListModel):
    def __init__(self, models: List[Model]):
        super().__init__()
        self._models = models

    def data(self, index, role = ...):
        model = self._models[index.row()]  # Get the object for the row
        if role == Qt.ItemDataRole.DisplayRole:
            return model.name
        if role == Qt.ItemDataRole.UserRole:
            return model

    def rowCount(self, parent= ...):
        return len(self._models)

    def add_model(self, model: Model):
        self.beginInsertRows(QModelIndex(), len(self._models), len(self._models))
        self._models.append(model)
        self.endInsertRows()