from pathlib import Path

from pandas import DataFrame


class EventLog:
    def __init__(self, name: str):
        self.name = name