from PySide6.QtWidgets import QTabWidget, QWidget, QHBoxLayout


class MainContentWidget(QWidget):
    def __init__(self, tabs_widget: QTabWidget):
        super().__init__()
        self.hbox_layout = QHBoxLayout()
        self.setLayout(self.hbox_layout)

        # ViewModels
        #self.event_log_list_viewmodel =

        #tabs_widget.setTabPosition(QTabWidget.TabPosition.South)
        #self.vbox_layout.addWidget(tabs_widget)