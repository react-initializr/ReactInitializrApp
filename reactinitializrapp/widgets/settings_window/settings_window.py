from PySide6.QtWidgets import QMainWindow

from reactinitializrapp.widgets.settings_window.ui_settings_window import UISettingsWindow


class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        self.ui = UISettingsWindow(self)
