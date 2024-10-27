import pm4py
from pm4py import DcrGraph


def load(path: list) -> DcrGraph:
    """
    Loads a DCR graph from a file containing event logs specified by a path.

    :param path: the path to the file containing the event log
    :return: the DCR graph
    :rtype: DcrGraph
    """
    log = pm4py.read_xes(path[0])
    graph, _ = pm4py.discover_dcr(log)
    return graph

