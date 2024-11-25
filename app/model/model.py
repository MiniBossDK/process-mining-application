from pandas import DataFrame
from pm4py import DcrGraph


class Model:
    def __init__(self, name: str, model: DataFrame):
        self.name = name
        self.model = model