from pandas import DataFrame

from app.model import EventLog
from pm4py import DcrGraph


class Model:
    def __init__(self, name: str, model: DataFrame, event_log: EventLog):
        self.name = name
        self.model = model
        self.event_log = event_log