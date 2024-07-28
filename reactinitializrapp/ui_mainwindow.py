from PySide6 import QtCore, QtWidgets
from reactinitializrapp.widgets.lateral_bar.lateral_bar import LateralBar


class UIMainWindow:
    def __init__(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("CentralWidget")

        self.lateral_bar = LateralBar(main_window)

        main_window.setCentralWidget(self.central_widget)
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    @staticmethod
    def retranslate_ui(main_window):
        _translate = QtCore.QCoreApplication.translate
        # Renombrar la ventana principal
        main_window.setWindowTitle(_translate("MainWindow", "React Initializr"))
