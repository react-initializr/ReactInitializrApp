from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QMovie
from PySide6.QtCore import Qt


class Ui_LoaderWidget(QWidget):
    def setupUi(self, LoaderWidget):
        # Configuración del layout principal
        self.mainLayout = QVBoxLayout(LoaderWidget)
        self.mainLayout.setObjectName("mainLayout")

        # Espaciador superior para centrar verticalmente
        verticalSpacerTop = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mainLayout.addItem(verticalSpacerTop)

        # Crear un layout horizontal para centrar horizontalmente
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Espaciador izquierdo para centrar horizontalmente
        horizontalSpacerLeft = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(horizontalSpacerLeft)

        # Crear un QLabel para mostrar el GIF
        self.loader_label = QLabel(LoaderWidget)
        self.loader_label.setObjectName("loader_label")
        self.loader_label.setFixedSize(80, 80)  # Cambia las dimensiones aquí según tus necesidades

        # Añadir el QLabel al layout horizontal
        self.horizontalLayout.addWidget(self.loader_label)

        # Espaciador derecho para centrar horizontalmente
        horizontalSpacerRight = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(horizontalSpacerRight)

        # Añadir el layout horizontal al layout principal
        self.mainLayout.addLayout(self.horizontalLayout)

        # Espaciador inferior para centrar verticalmente
        verticalSpacerBottom = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mainLayout.addItem(verticalSpacerBottom)

        # Configurar el GIF de carga
        self.loader_movie = QMovie("assets/icons/loader.gif")  # Asegúrate de que el GIF esté en esta ruta
        self.loader_movie.setScaledSize(self.loader_label.size())  # Escalar el GIF al tamaño del QLabel
        self.loader_label.setMovie(self.loader_movie)
        self.loader_movie.start()  # Iniciar la animación