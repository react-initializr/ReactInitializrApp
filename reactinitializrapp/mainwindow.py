from reactinitializrapp.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals and slots
        self.ui.someButton.clicked.connect(self.some_button_clicked)

    def some_button_clicked(self):
        print("Application works")
