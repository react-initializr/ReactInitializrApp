from PySide6 import QtCore, QtWidgets

from reactinitializrapp.utils.store import Store
from reactinitializrapp.widgets.search_input.search_input import SearchInput
from reactinitializrapp.widgets.project_button.project_button import ProjectButton
from reactinitializrapp.models.project import Project


class UILateralBar:
    def __init__(self, lateral_bar):
        lateral_bar.setObjectName("LateralBar")
        self.setup_ui(lateral_bar)
        self.setup_styles()

    def setup_ui(self, lateral_bar):
        # Disposición Vertical
        self.vertical_layout = QtWidgets.QVBoxLayout(lateral_bar)
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)

        # Widget contenedor
        self.container_widget = QtWidgets.QWidget(lateral_bar)

        # Layout para el contenedor
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)

        # Búsqueda
        self.search_input = SearchInput(self.container_widget)

        # Proyectos de prueba
        # TODO:
        #  - Agregar un layout para los proyectos
        self.projects = self.get_projects()

        # Botones
        self.btn_new_project = QtWidgets.QPushButton("NP")
        self.btn_logo = QtWidgets.QPushButton("React Initializr >")

        # Añadir los botones al layout del contenedor
        self.container_layout.addWidget(self.btn_new_project)

        # Añadir los proyectos al layout del contenedor
        for project in self.projects:
            project_button = ProjectButton(project)
            self.container_layout.addWidget(project_button)

        self.container_layout.addWidget(self.btn_logo)

        # Ocultar el botón de nuevo proyecto al inicio por estar activo
        self.btn_new_project.hide()

        # Añadir el contenedor al layout principal
        self.vertical_layout.addWidget(self.container_widget)

        # Ajustar el tamaño del lateral_bar al tamaño de la ventana principal
        lateral_bar.setSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding
        )
        lateral_bar.setMaximumWidth(200)

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
            """
            QPushButton {
                background-color: transparent; color: white; padding: 10px 0; border: none;
            }
            QPushButton:hover {
                background-color: #292929;
                border-radius: 5px;
            }
            """
        )

    def get_projects(self):
        projects = []

        store = Store()  # Obtener la instancia de Store

        # Obtener los proyectos de la base de datos
        projects = store.get_state()["projects"]

        return projects
