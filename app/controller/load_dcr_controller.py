import pm4py
from pm4py import DcrGraph
from pm4py.objects.log.obj import EventLog
from pm4py.visualization.dcr import visualizer as dcr_visualizer


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

    graph, _ = pm4py.discover_dcr(event_log)

    # Visualize the DCR graph
    gviz = dcr_visualizer.apply(graph)
    dcr_visualizer.view(gviz)

    return graph