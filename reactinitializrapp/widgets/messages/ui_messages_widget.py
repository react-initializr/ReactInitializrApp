from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from PySide6.QtGui import QFont


class Ui_MessagesWidget(QWidget):
    def setupUi(self, MessagesWidget):
        # Configuración del layout
        self.verticalLayout = QVBoxLayout(MessagesWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.chatHistory = QListWidget(MessagesWidget)
        self.chatHistory.setObjectName("chatHistory")
        self.chatHistory.setStyleSheet(
            "background-color: Transparent; padding: 10px; border-radius: 5px; color: white;")
        self.verticalLayout.addWidget(self.chatHistory)
