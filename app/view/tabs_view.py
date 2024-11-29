from PySide6.QtWidgets import QWidget, QTabWidget, QMessageBox, QVBoxLayout


class TabsView(QWidget):
    def __init__(self, views):
        super().__init__()

        self.views = views
        self.tab_widget = QTabWidget()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tab_widget)
        self.setLayout(self.layout)

        self.closeable_tabs = []
        for view in views:
            tab = QTabWidget()
            tab.setTabsClosable(view.closeable())
            if view.closeable():
                self.closeable_tabs.append(tab)
            self.tab_widget.addTab(view, view.tab_name())

        for tab in self.closeable_tabs:
            tab.tabCloseRequested.connect(self.close_tab)

        self.updatesEnabled()

    def close_tab(self, index):
        confirm = QMessageBox.question(
            self,
            "Close Tab",
            f"Are you sure you want to close the '{self.tab_widget.tabText(index)}' tab?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.tab_widget.removeTab(index)

        else:
            # Optionally, prevent closing other tabs or handle differently
            QMessageBox.information(
                self,
                "Cannot Close Tab",
                "This tab cannot be closed."
            )