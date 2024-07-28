from PySide6 import QtWidgets
from reactinitializrapp.widgets.lateral_bar.ui_lateral_bar import UILateralBar


class LateralBar(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("LateralBar")
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
            self.setGeometry(0, 0, 100, 600)
            self.ui.btn_new_project.setText("NP")
            self.ui.btn_logo.setText("L")
            self.is_active = False
        else:
            self.setGeometry(0, 0, 200, 600)
            self.ui.btn_new_project.setText("New Project")
            self.ui.btn_logo.setText("Logo")
            self.is_active = True

    def on_new_project_clicked(self):
        print("New Project clicked")

    def on_logo_clicked(self):
        print("Logo clicked")
