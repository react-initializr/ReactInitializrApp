from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QFrame, QGraphicsDropShadowEffect, QListWidget, QListWidgetItem, QLabel
from PySide6.QtGui import QFont, QIcon, QColor, QFontDatabase
from PySide6.QtCore import QSize, Qt, QDateTime


class Ui_ChatWidget(QWidget):
    def setupUi(self, ChatWidget):
        # Cargar la fuente personalizada
        QFontDatabase.addApplicationFont("assets/fonts/Poppins/Poppins-Regular.ttf")
        font = QFont("Poppins", 10)

        ChatWidget.setObjectName("ChatWidget")
        self.verticalLayout = QVBoxLayout(ChatWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.chatHistory = QListWidget(ChatWidget)
        self.chatHistory.setObjectName("chatHistory")
        self.chatHistory.setStyleSheet("background-color: Transparent; padding: 10px; border-radius: 5px; color: white;")
        self.chatHistory.setFont(font)
        self.chatHistory.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Ocultar barra de desplazamiento vertical
        self.chatHistory.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Ocultar barra de desplazamiento horizontal
        self.verticalLayout.addWidget(self.chatHistory)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.messageInputFrame = QFrame(ChatWidget)
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
        self.messageInput.setFont(font)
        self.messageInputLayout.addWidget(self.messageInput)

        self.messageInput.returnPressed.connect(self.send_message)


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
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChatWidget)
        self.sendButton.clicked.connect(self.send_message)

    def retranslateUi(self, ChatWidget):
        ChatWidget.setWindowTitle("Chat")

    def send_message(self):
        message = self.messageInput.text()
        if message:
            self.add_message(message, is_sender=True)
            self.messageInput.clear()

    def add_message(self, message, is_sender=True):
        # Obtener la hora actual
        current_time = QDateTime.currentDateTime().toString("HH:mm")

        font = QFont("Poppins", 10)
        item = QListWidgetItem()
        item_widget = QWidget()
        item_layout = QVBoxLayout(item_widget)  # Usar QVBoxLayout para la alineación vertical
        item_layout.setContentsMargins(10, 10, 10, 10)

        # Crear el mensaje con la hora
        message_text = QLabel(f"{message}")
        message_text.setStyleSheet(f"""
            background-color: {"#3e3e3e" if is_sender else "#2e2e2e"};
            color: white;
            padding: 10px;
            border-radius: 15px;
            max-width: 600px;
            word-wrap: break-word;
            text-align: left;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        """)
        message_text.setFont(font)
        message_text.setWordWrap(True)  # Habilitar el ajuste de línea

        # Aplicar un efecto de sombra directamente al QLabel
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(10)
        shadow_effect.setXOffset(2)
        shadow_effect.setYOffset(2)
        shadow_effect.setColor(QColor(0, 0, 0, 160))
        message_text.setGraphicsEffect(shadow_effect)

        # Crear la etiqueta de la hora
        time_label = QLabel(current_time)
        time_label.setStyleSheet("color: gray; font-size: 8pt;")
        time_label.setFont(font)

        # Crear el mensaje con la hora
        message_text = QLabel(f"{message}")
        if is_sender:
            message_text.setStyleSheet("""
                background-color: #3e3e3e;
                color: white;
                padding: 10px;
                border-radius: 15px;
                max-width: 600%;
                word-wrap: break-word;
                text-align: left;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            """)
        else:
            message_text.setStyleSheet("""
                background-color: transparent;
                color: white;
                padding: 10px;
                word-wrap: break-word;
                text-align: left;
            """)
        message_text.setFont(font)
        message_text.setWordWrap(True)  # Habilitar el ajuste de línea

        if is_sender:
            # Aplicar un efecto de sombra directamente al QLabel solo para mensajes enviados
            shadow_effect = QGraphicsDropShadowEffect()
            shadow_effect.setBlurRadius(10)
            shadow_effect.setXOffset(2)
            shadow_effect.setYOffset(2)
            shadow_effect.setColor(QColor(0, 0, 0, 160))
            message_text.setGraphicsEffect(shadow_effect)

        # Alineación horizontal de hora y texto
        horizontal_layout = QHBoxLayout()
        if is_sender:
            horizontal_layout.addWidget(message_text)
            horizontal_layout.addWidget(time_label)
            horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:
            horizontal_layout.addWidget(time_label)
            horizontal_layout.addWidget(message_text)
            horizontal_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        item_layout.addLayout(horizontal_layout)

        item.setSizeHint(item_widget.sizeHint())
        self.chatHistory.addItem(item)
        self.chatHistory.setItemWidget(item, item_widget)
