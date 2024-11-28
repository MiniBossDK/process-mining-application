from pathlib import Path
from typing import Tuple

from PySide6.QtCore import QObject, Signal

import pm4py
from app.model import PetriNetModel
from app.model.dcr_model import DcrModel
from app.model.repositories.dcr_model_repository import DcrModelRepository
from app.model.repositories.petrinet_model_repository import PetriNetModelRepository


class ModelListViewModel(QObject):
    selected_dcr_model_changed = Signal(DcrModel)
    selected_petri_net_model_changed = Signal(PetriNetModel)

    dcr_model_added = Signal(DcrModel)
    petri_net_model_added = Signal(PetriNetModel)

    def __init__(self, dcr_model_repository: DcrModelRepository, petri_net_model_repository: PetriNetModelRepository):
        super().__init__()
        self._dcr_model_repository = dcr_model_repository
        self._petri_net_model_repository = petri_net_model_repository

    def perform_discovery_dcr(self, path: Path):
        graph, _ = pm4py.discover_dcr(self.load_xes_file(path))
        return graph

    def perform_discovery_petri_net(self, path: Path):
        df = self.load_xes_file(path)
        net, im, fm = pm4py.discover_petri_net_inductive(df)
        alignments_diagnostics = pm4py.conformance_diagnostics_alignments(df, net, im, fm)
        return (net, im, fm), alignments_diagnostics

    def load_xes_file(self, path: Path):
        return pm4py.read_xes(path.__str__())

    def add_dcr_model(self, path: Path):
        model = DcrModel(path.name, self.perform_discovery_dcr(path))
        self._dcr_model_repository.add_model(model)
        self.dcr_model_added.emit(model)

    def add_petri_net_model(self, path: Path):
        petri_net, aligned_traces = self.perform_discovery_petri_net(path)
        model = PetriNetModel(path.name, petri_net, aligned_traces)
        self._petri_net_model_repository.add_model(model)
        self.petri_net_model_added.emit(model)

    def set_selected_dcr_model(self, model: DcrModel):
        self._dcr_model_repository.set_selected_model(model)
        self.selected_dcr_model_changed.emit(model)

    def set_selected_petri_net_model(self, model: PetriNetModel):
        self._petri_net_model_repository.set_selected_model(model)
        self.selected_petri_net_model_changed.emit(model)
