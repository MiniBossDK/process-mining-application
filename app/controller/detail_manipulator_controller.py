from PySide6.QtCore import Slot


class detail_manipulator_controller():
    def __init__(self, view):
        self.view = view
        self.view.button.clicked.connect(self.handle_roles)
        self.view.button2.clicked.connect(self.handle_pending)
        self.view.button3.clicked.connect(self.handle_timed)

    @Slot()
    def handle_roles(self):
        print('Roles')

    @Slot()
    def handle_pending(self):
        print('Pending')

    @Slot()
    def handle_timed(self):
        print('Timed')
