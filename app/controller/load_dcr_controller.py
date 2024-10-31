import pm4py
from pm4py.visualization.dcr import visualizer as dcr_visualizer
import os

def save_gviz_as_svg(gviz, output_path):
    # Remove the extension if it exists
    if output_path.endswith('.svg'):
        output_path = output_path[:-4]
    gviz.render(output_path, format='svg')

    # Delete the intermediate file if it exists
    intermediate_file = output_path
    if os.path.exists(intermediate_file):
        os.remove(intermediate_file)

def handle_load(path: str):
    event_log = pm4py.read_xes(path)

    graph, _ = pm4py.discover_dcr(event_log)

    # Visualize the DCR graph
    gviz = dcr_visualizer.apply(graph)
    save_gviz_as_svg(gviz, 'output.svg')