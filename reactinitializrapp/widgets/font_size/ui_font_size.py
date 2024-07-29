from PySide6 import QtWidgets, QtCore


class UIFontSize:
    def __init__(self, font_size):
        font_size.setObjectName("FontSize")
        # font_size.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.setup_ui(font_size)
        self.setup_styles()

    def setup_ui(self, font_size):
        # Disposición Horizontal
        self.horizontal_layout = QtWidgets.QHBoxLayout(font_size)

        self.label = QtWidgets.QLabel("Tamaño de fuente")

        self.in_font_size = QtWidgets.QLineEdit()

        self.horizontal_layout.addWidget(self.label)
        self.horizontal_layout.addWidget(self.in_font_size)

    def setup_styles(self):
        # Estilos de Label
        self.label.setStyleSheet("border: none;")

        # Estilos de Input
        self.in_font_size.setStyleSheet("background-color: transparent; padding: 5px;")
