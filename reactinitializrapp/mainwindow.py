from reactinitializrapp.ui_mainwindow import UIMainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout


# Hereda de QMainWindow
class MainWindow(QMainWindow):
    # Constructor
    def __init__(self):
        # Llama al constructor de la clase padre QMainWindow
        super(MainWindow, self).__init__()
        # Instancia la clase UIMainWindow
        self.ui = UIMainWindow(self)
