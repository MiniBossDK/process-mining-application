from pathlib import Path

from pandas import DataFrame


class EventLog:
    def __init__(self, name: str, path: Path, data: DataFrame):
        self.name = name
        self.path = path
        self.data = data