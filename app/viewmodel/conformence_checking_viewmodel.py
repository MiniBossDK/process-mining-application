from pathlib import Path

from PySide6.QtCore import QObject, Signal

import pm4py
from app.model import EventLog, PetriNetModel


class ConformanceCheckingViewModel(QObject):

    alignment_image_saved = Signal(Path)

    def __init__(self):
        super().__init__()

    def alignment_conformance_checking(self, event_log: EventLog, model: PetriNetModel):
        path = Path('alignment_output.svg')
        pm4py.save_vis_alignments(event_log.data, model.aligned_traces, path.absolute().__str__())
        self.alignment_image_saved.emit(path)