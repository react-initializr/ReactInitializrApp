from PySide6 import QtWidgets, QtCore

from reactinitializrapp.widgets.font_size.font_size import FontSize


class UISettingsWindow:
    def __init__(self, settings_window):
        settings_window.setObjectName("SettingsWindow")
        settings_window.resize(600, 400)
        self.setup_ui(settings_window)
        self.setup_styles()
        self.retranslate_ui(settings_window)

    @staticmethod
    def retranslate_ui(settings_window):
        _translate = QtCore.QCoreApplication.translate
        # Renombrar la ventana de ajustes
        settings_window.setWindowTitle(_translate("SettingsWindow", "Ajustes"))

    def setup_ui(self, settings_window):
        # Contenedor central
        self.central_widget = QtWidgets.QWidget(settings_window)
        self.central_widget.setObjectName("CentralWidget")

        # Disposición Vertical
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)

        # Título de la ventana
        self.title = QtWidgets.QLabel("React Initializr")

        # Widget contenedor para opciones de fuente
        self.font_container = QtWidgets.QWidget()
        self.font_container.setObjectName("FontWidget")

        # Disposición Vertical para opciones de fuente
        self.font_layout = QtWidgets.QVBoxLayout(self.font_container)

        self.font_size = FontSize()

        # Añadir las opciones de fuente al layout vertical
        self.font_layout.addWidget(self.font_size)

        # Estructura de la ventana de ajustes en el layout vertical
        self.vertical_layout.addWidget(self.title)
        self.vertical_layout.addWidget(self.font_container)

        settings_window.setCentralWidget(self.central_widget)

    def setup_styles(self):
        # Estilos para el título
        self.title.setStyleSheet(
            "font-size: 20px; font-weight: bold; padding: 10px auto;"
        )

        # Estilos para el contenedor de opciones de fuente
        self.font_container.setStyleSheet("border: none; padding: 10px;")
