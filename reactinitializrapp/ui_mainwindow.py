from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QGraphicsBlurEffect
from reactinitializrapp.widgets.chat.chat import ChatWidget


class UIMainWindow:
    def __init__(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("CentralWidget")

        # Crear un layout vertical para central_widget
        self.verticalLayout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_widget.setLayout(self.verticalLayout)

        self.chatWidget = ChatWidget(self.central_widget)
        self.verticalLayout.addWidget(self.chatWidget)

        main_window.setCentralWidget(self.central_widget)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    @staticmethod
    def retranslate_ui(main_window):
        _translate = QtCore.QCoreApplication.translate
        # Renombrar la ventana principal
        main_window.setWindowTitle(_translate("MainWindow", "React Initializr"))
