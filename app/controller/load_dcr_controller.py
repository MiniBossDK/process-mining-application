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

def handle_load(file_paths):
    for file_path in file_paths:
        event_log = pm4py.read_xes(file_path)