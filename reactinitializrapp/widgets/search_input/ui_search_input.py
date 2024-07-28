from PySide6 import QtWidgets, QtCore


class UISearchInput:
    def __init__(self, search_input):
        search_input.setGeometry(QtCore.QRect(0, 0, 180, 100))
        self.setup_ui(search_input)
        self.setup_styles()

    def setup_ui(self, search_input):
        # Disposición Horizontal
        self.horizontal_layout = QtWidgets.QHBoxLayout(search_input)

        # Widget contenedor
        self.container_widget = QtWidgets.QWidget(search_input)

        # Layout para el contenedor
        self.container_layout = QtWidgets.QHBoxLayout(self.container_widget)

        # Campo de texto
        self.txt_search = QtWidgets.QLineEdit()

        # Botón
        # TODO: Cambiar el texto del botón a un icono
        self.btn_search = QtWidgets.QPushButton("S")

        # Añadir el campo de texto y el botón al layout del contenedor
        self.container_layout.addWidget(self.txt_search)
        self.container_layout.addWidget(self.btn_search)

        # Añadir el contenedor al layout principal
        self.horizontal_layout.addWidget(self.container_widget)

    def setup_styles(self):
        # Estilos para el widget contenedor
        self.container_widget.setStyleSheet("border: none; padding: 0;")

        # Estilos para el campo de texto
        self.txt_search.setStyleSheet(
            "padding: 5px; border-bottom: 1px solid #000; border-radius: 0; background-color: transparent;"
        )

        # Estilos para el botón
        self.btn_search.setStyleSheet(
            "background-color: transparent; color: white; padding: 5px 10px; border-radius: 5px;"
        )
