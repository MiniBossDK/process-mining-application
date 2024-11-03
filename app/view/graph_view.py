from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import Qt

class GraphicsView(QGraphicsView):
    def __init__(self, slider, scene, *args, **kwargs):
        super(GraphicsView, self).__init__(scene, *args, **kwargs)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.slider = slider

    def wheelEvent(self, event):
        if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
            if event.angleDelta().y() > 0:
                new_value = min(self.slider.value() + 10, self.slider.maximum())
            else:
                new_value = max(self.slider.value() - 10, self.slider.minimum())
            self.slider.setValue(new_value)
        else:
            super(GraphicsView, self).wheelEvent(event)







