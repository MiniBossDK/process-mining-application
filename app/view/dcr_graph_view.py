from PIL.ImageQt import QPixmap

import pm4py


class DCRGraphView(QPixmap):
    def __init__(self):
        super().__init__()
        graph, _ = pm4py.discover_dcr()