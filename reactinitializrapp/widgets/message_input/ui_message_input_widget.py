from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QHBoxLayout, QFrame, QGraphicsDropShadowEffect
from PySide6.QtGui import QFont, QIcon, QColor
from PySide6.QtCore import QSize


class Ui_MessageInputWidget(QWidget):
    def setupUi(self, MessageInputWidget):
        self.horizontalLayout = QHBoxLayout(MessageInputWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.messageInputFrame = QFrame(MessageInputWidget)
        self.messageInputFrame.setObjectName("messageInputFrame")
        self.messageInputFrame.setStyleSheet("""
            QFrame {
                border: 0px solid #cccccc;
                border-radius: 20px;
                padding: 0px;
                background-color: #3e3e3e;
            }
            QLineEdit {
                border: none;
                padding: 5px;
                font-size: 12pt;
                background-color: #3e3e3e;
                color: white;
            }
            QPushButton {
                border: none;
                padding: 10px;
                font-size: 12pt;
                color: white;
                background-color: #fff;
                border-radius: 15px;
                margin-left: 5px;
            }
        """)
        self.messageInputLayout = QHBoxLayout(self.messageInputFrame)
        self.messageInput = QLineEdit(self.messageInputFrame)
        self.messageInput.setObjectName("messageInput")
        self.messageInput.setPlaceholderText("Type your message here...")
        font = QFont("Poppins", 10)
        self.messageInput.setFont(font)
        self.messageInputLayout.addWidget(self.messageInput)

        # Crear un efecto de sombra
        shadow = QGraphicsDropShadowEffect(self.messageInputFrame)
        shadow.setBlurRadius(10)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.messageInputFrame.setGraphicsEffect(shadow)

        self.sendButton = QPushButton(self.messageInputFrame)
        self.sendButton.setObjectName("sendButton")
        self.sendButton.setText("")
        self.sendButton.setIcon(QIcon("assets/icons/paper_plane.png"))  # Ajusta la ruta según sea necesario
        self.sendButton.setIconSize(QSize(20, 20))  # Ajusta el tamaño del icono según sea necesario
        self.sendButton.setFont(font)

        # Crear un efecto de sombra
        shadow = QGraphicsDropShadowEffect(self.sendButton)
        shadow.setBlurRadius(10)
        shadow.setXOffset(3)
        shadow.setYOffset(3)
        shadow.setColor(QColor(0, 0, 0, 100))
        self.sendButton.setGraphicsEffect(shadow)

        self.messageInputLayout.addWidget(self.sendButton)
        self.horizontalLayout.addWidget(self.messageInputFrame)
