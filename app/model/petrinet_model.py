from typing import Any

from pm4py import PetriNet, Marking


class PetriNetModel:
    def __init__(self, name: str, petri_net: tuple[PetriNet, Marking, Marking], aligned_traces: Any):
        self.name = name
        self.petri_net = petri_net
        self.aligned_traces = aligned_traces