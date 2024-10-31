import pm4py
from pm4py import DcrGraph
from pm4py.objects.log.obj import EventLog


def load(path: str) -> EventLog:
    """
    Loads a DCR graph from a file containing event logs specified by a path.

    :param path: the path to the file containing the event log
    :return: the DCR graph
    :rtype: DcrGraph
    """
    return pm4py.read_xes(path)


def handle_load(path: str):
    event_log = load(path)
    return None # TODO - Handle the