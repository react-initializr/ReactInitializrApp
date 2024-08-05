from PySide6 import QtWidgets

from reactinitializrapp.models.project import Project
from reactinitializrapp.utils.actions import add_project
from reactinitializrapp.utils.store import Store
from reactinitializrapp.widgets.lateral_bar.ui_lateral_bar import UILateralBar
from reactinitializrapp.widgets.settings_window.settings_window import SettingsWindow


class LateralBar(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = UILateralBar(self)

        # Atributo para saber si el widget está activo
        self._is_active = True

        # Conectar eventos
        self.ui.btn_new_project.clicked.connect(self.on_new_project_clicked)
        self.ui.btn_logo.clicked.connect(self.on_logo_clicked)

    # Getter para el atributo _is_active
    @property
    def is_active(self):
        return self._is_active

    # Setter para el atributo _is_active
    @is_active.setter
    def is_active(self, value):
        if isinstance(value, bool):
            self._is_active = value
        else:
            raise ValueError("The value must be a boolean")

    # Sobreescribir el evento mousePressEvent
    def mousePressEvent(self, event):
        self.on_lateral_bar_clicked()

    def on_lateral_bar_clicked(self):
        if self.is_active:
            self.setFixedWidth(100)
            self.ui.btn_new_project.show()
            self.ui.search_input.hide()
            self.ui.btn_logo.setText("L")
            self.ui.btn_logo.setStyleSheet(
                "background-color: #292929; color: white; border: 1px solid #000; padding: 10px 0; border-radius: 5px;"
            )
            self.is_active = False
        else:
            self.setFixedWidth(200)
            self.ui.btn_new_project.hide()
            self.ui.search_input.show()
            self.ui.btn_logo.setText("React Initializr >")
            self.ui.btn_logo.setStyleSheet(
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
            self.is_active = True

    def on_new_project_clicked(self):
        # Crear una nueva instancia de Project
        new_project = Project("New Project")

        store = Store()  # Obtener la instancia de Store

        # Añadir el proyecto a la base de datos
        store.dispatch(add_project(new_project))

        print(new_project)

    def on_logo_clicked(self):
        # Mostrar la ventana de configuración
        self.settings_window = SettingsWindow()
        self.settings_window.show()
