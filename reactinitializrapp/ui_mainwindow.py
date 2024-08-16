from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGraphicsBlurEffect

from reactinitializrapp.widgets.lateral_bar.lateral_bar import LateralBar
from reactinitializrapp.widgets.chat.chat import ChatWidget

class UIMainWindow:
    def __init__(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)
        self.setup_ui(main_window)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    @staticmethod
    def retranslate_ui(main_window):
        _translate = QtCore.QCoreApplication.translate
        # Renombrar la ventana principal
        main_window.setWindowTitle(_translate("MainWindow", "React Initializr"))

    def setup_ui(self, main_window):
        # Contenedor central
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("CentralWidget")

        # Disposición Horizontal principal
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.central_widget)

        # Lateral Bar a la izquierda
        self.lateral_bar = LateralBar(self.central_widget)
        self.horizontal_layout.addWidget(self.lateral_bar)

        # Chat a la derecha
        self.chatWidget = ChatWidget(self.central_widget)
        self.horizontal_layout.addWidget(self.chatWidget)

        main_window.setCentralWidget(self.central_widget)

