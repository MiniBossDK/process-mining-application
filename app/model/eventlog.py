from pathlib import Path

from pandas import DataFrame


class EventLog:
    def __init__(self, name: str, data: DataFrame):
        self.name = name
        self.data = data