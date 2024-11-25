from pm4py import DcrGraph


class Model:
    def __init__(self, name: str, model: DcrGraph):
        self.name = name
        self.model = model