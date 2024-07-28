from PySide6 import QtCore, QtWidgets


class UILateralBar:
    def __init__(self, lateral_bar):
        lateral_bar.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.setup_ui(lateral_bar)
        self.setup_styles()

    def setup_ui(self, lateral_bar):
        # Disposición Vertical
        self.vertical_layout = QtWidgets.QVBoxLayout(lateral_bar)

        # Widget contenedor
        self.container_widget = QtWidgets.QWidget(lateral_bar)

        # Layout para el contenedor
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)

        # Botones
        self.btn_new_project = QtWidgets.QPushButton("New Project")
        self.btn_logo = QtWidgets.QPushButton("Logo")

        # Añadir los botones al layout del contenedor
        self.container_layout.addWidget(self.btn_new_project)
        self.container_layout.addWidget(self.btn_logo)

        # Añadir el contenedor al layout principal
        self.vertical_layout.addWidget(self.container_widget)

    def setup_styles(self):
        # Estilos para el widget contenedor
        self.container_widget.setStyleSheet(
            "border: 1px solid #000; border-radius: 5px;"
        )

        # Estilos para los botones
        self.btn_new_project.setStyleSheet(
            "background-color: #292929; color: white; border: 1px solid #000; padding: 10px 0; border-radius: 5px;"
        )
        self.btn_logo.setStyleSheet(
            "background-color: #292929; color: white; border: 1px solid #000; padding: 10px 0; border-radius: 5px;"
        )
