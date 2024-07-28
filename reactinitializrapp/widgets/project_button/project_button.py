from PySide6 import QtWidgets, QtCore

from reactinitializrapp.models.project import Project

from reactinitializrapp.widgets.project_button.ui_project_button import UIProjectButton


class ProjectButton(QtWidgets.QPushButton):
    def __init__(self, project: Project, parent=None):
        super().__init__(parent)
        self.ui = UIProjectButton(self, project)
        self.clicked.connect(self.select_project)

    def select_project(self):
        print("Select Project")

    # Sobreescribir el evento mousePressEvent
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            self.show_context_menu()
        else:
            super().mousePressEvent(event)

    def show_context_menu(self):
        menu = QtWidgets.QMenu(self)
        pin = menu.addAction("Pin")
        change_name = menu.addAction("Cambiar nombre")
        archive = menu.addAction("Archivar")
        delete = menu.addAction("Eliminar")

        action = menu.exec_(self.mapToGlobal(self.rect().bottomRight()))

        if action == pin:
            print("Pin selected")
        elif action == change_name:
            print("Change name selected")
        elif action == archive:
            print("Archive selected")
        elif action == delete:
            print("Delete selected")
