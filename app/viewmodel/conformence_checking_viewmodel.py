from pathlib import Path

from PySide6.QtCore import QObject, Signal

import pm4py
from app.model import EventLog, DcrModel, EventLogRepository, PetriNetModel
from app.model.repositories.dcr_model_repository import DcrModelRepository


class ConformanceCheckingViewModel(QObject):

    alignment_image_saved = Signal(Path)

    def __init__(self, event_log: EventLogRepository, model: DcrModelRepository):
        super().__init__()
        self.event_dcr_graph = None
        self.model_dcr_graph = None
        self.event_log = None
        self.model_log = None
        self.event_log_loaded = False
        self.model_log_loaded = False
        self.active_event_log = None
        self.active_model_log= None

    def set_event_log_loaded(self, loaded, event_log: EventLog):
        self.event_log_loaded = loaded
        self.event_log = event_log
        self.event_dcr_graph, _ = pm4py.discover_dcr(self.event_log.data)

    def set_model_log_loaded(self, loaded, model_log: DcrModel):

        self.model_log_loaded = loaded
        self.model_log = model_log

        self.model_dcr_graph = model_log

    def set_active_event_log(self, event_log: EventLog):
        self.active_event_log = event_log

    def set_active_model_log(self, model_log: DcrModel):
        self.active_model_log = model_log

    def alignment_conformance_checking(self, event_log: EventLog, model: PetriNetModel):

        path = Path('alignment_output.svg')
        pm4py.save_vis_alignments(event_log.data, model.aligned_traces, path.absolute().__str__())
        self.alignment_image_saved.emit(path)