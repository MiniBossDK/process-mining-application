from PySide6.QtCore import QObject, Signal

from app.model.model import Model
from app.model.repositories.model_repository import ModelRepository


class ModelListViewModel(QObject):
    selected_model_changed = Signal(Model)
    model_added = Signal(Model)

    def __init__(self, model: ModelRepository):
        super().__init__()
        self._model = model

    def add_model(self, model: Model):
        self._model.add_model(model)
        self.model_added.emit(model)

    def set_selected_model(self, model: Model):
        self._model.selected_model = model
        self.selected_model_changed.emit(model)