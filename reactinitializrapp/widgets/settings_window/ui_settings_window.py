from PySide6 import QtWidgets, QtCore


class UISettingsWindow:
    def __init__(self, settings_window):
        settings_window.setObjectName("SettingsWindow")
        settings_window.resize(600, 400)

        self.central_widget = QtWidgets.QWidget(settings_window)
        self.central_widget.setObjectName("CentralWidget")

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.label = QtWidgets.QLabel("This is the secondary window", self.central_widget)

        self.layout.addWidget(self.label)

        settings_window.setCentralWidget(self.central_widget)
        self.retranslate_ui(settings_window)

    @staticmethod
    def retranslate_ui(settings_window):
        _translate = QtCore.QCoreApplication.translate
        # Renombrar la ventana de ajustes
        settings_window.setWindowTitle(_translate("SettingsWindow", "Ajustes"))
