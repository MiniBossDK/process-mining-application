from pandas import DataFrame


class EventLog:
    def __init__(self, name: str, data: DataFrame, is_selected: bool):
        self.name = name
        self.data = data
        self.is_selected = is_selected