from pathlib import Path

from pandas import DataFrame


class EventLog:
    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path