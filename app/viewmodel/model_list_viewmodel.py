from pathlib import Path

from PySide6.QtCore import QObject, Signal

import pm4py
from app.model import EventLog
from app.model.model import Model
from app.model.repositories.model_repository import ModelRepository


class ModelListViewModel(QObject):
    selected_model_changed = Signal(Model)
    model_added = Signal(Model)

    def __init__(self, model: ModelRepository):
        super().__init__()
        self._model = model

    def perform_discovery(self, path: Path):
        graph, _ = pm4py.discover_dcr(self.load_xes_file(path))
        return graph

    def load_xes_file(self, path: Path):
        return pm4py.read_xes(path.__str__())


    def add_model(self, model: Model):
        self._model.add_model(model)
        self.model_added.emit(model)

    def set_selected_model(self, model: Model):
        self._model.selected_model = model
        self.selected_model_changed.emit(model)