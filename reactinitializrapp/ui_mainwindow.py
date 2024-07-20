from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("CentralWidget")

        # Directory button
        self.directory_button = QtWidgets.QPushButton(self.central_widget)
        self.directory_button.setGeometry(QtCore.QRect(100, 100, 200, 40))
        self.directory_button.setObjectName("DirectoryButton")

        # Text browser
        self.text_browser = QtWidgets.QTextBrowser(self.central_widget)
        self.text_browser.setGeometry(QtCore.QRect(50, 150, 700, 400))
        self.text_browser.setObjectName("TextBrowser")

        MainWindow.setCentralWidget(self.central_widget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "React Initializr"))
        self.directory_button.setText(_translate("MainWindow", "Choose directory..."))
        self.text_browser.setText(_translate("MainWindow", "Render Markdown here..."))
