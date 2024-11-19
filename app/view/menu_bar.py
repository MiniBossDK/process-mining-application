from PySide6.QtGui import QAction
from PySide6.QtWidgets import QFileDialog, QMenuBar, QMessageBox

class MenuBar(QMenuBar):
    def _init_(self, example_instance):
        super()._init_()
        self.example_instance = example_instance
        font = self.font()
        font.setPointSize(18)
        self.setFont(font)
        load_action = QAction('Load Event Log', self)
        load_action.setStatusTip('Load Event Log')
        load_action.triggered.connect(self.open_file_dialog)

        file_menu = self.addMenu('File')
        file_menu.addAction(load_action)
        self.show()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("All Event Log files (*.xes)")
        file_dialog.fileSelected.connect(self.handle_file_selected)
        file_dialog.exec()

    def handle_file_selected(self, file_path):
        try:
            data = self.parse_xes_file(file_path)
            if data:
                self.example_instance.current_file_path = file_path
                self.example_instance.data = data
                QMessageBox.information(self, "Success", "The Data has been loaded successfully!")
                self.example_instance.show_data()
            else:
                QMessageBox.information(self, "No Data", "No events found in the XES file.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load event log: {str(e)}")

    def parse_xes_file(self, file_path):
        import xml.etree.ElementTree as ET

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to parse XES file: {str(e)}")
            return None

        data = []
        for trace in root.findall('trace'):
            case_id = None
            for string in trace.findall('string'):
                if string.get('key') == 'concept:name':
                    case_id = string.get('value')
                    break
            if case_id is None:
                continue

            for event in trace.findall('event'):
                event_data = {'case_id': case_id}
                for child in event:
                    key = child.get('key')
                    value = child.get('value')
                    if key and value:
                        event_data[key] = value
                data.append(event_data)


        return data
