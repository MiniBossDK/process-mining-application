from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QMessageBox

import pm4py
from app.model import EventLog, EventLogListModel
from app.model.model import Model
from app.model.model_list import ModelList




class ModelListViewModel(QObject):
    selected_model_changed = Signal(Model)

    def __init__(self, model: ModelList):
        super().__init__()
        self._model = model
        self._selected_model = None

    @property
    def model(self):
        return self._model

    @property
    def selected_event_log(self):
        return self._selected_model

    def set_selected_model(self, index):
        if index.isValid():
            self._selected_model = self._model.data(index, Qt.ItemDataRole.UserRole)
            self.selected_model_changed.emit(self._selected_model)
            print(self._selected_model.name)

    def add_model(self, event_log: EventLog):
        try:
            #TODO
            print("hard coded value, fix for later")
            model, _ = pm4py.discover_dcr(event_log.data, post_process={'roles'}, group_key="org:resource")
        except Exception:
            return
        self._model.add_model(Model(event_log.name, model))


