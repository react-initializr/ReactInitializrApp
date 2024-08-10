from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QHBoxLayout, QFrame, \
    QGraphicsDropShadowEffect, QListWidget, QListWidgetItem, QLabel
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import QDateTime, Qt
from reactinitializrapp.widgets.messages.ui_messages_widget import Ui_MessagesWidget


class MessagesWidget(QWidget):
    def __init__(self, parent=None):
        super(MessagesWidget, self).__init__(parent)
        self.ui = Ui_MessagesWidget()
        self.ui.setupUi(self)

    def add_message(self, message, is_sender=True):

        print(f"add_message called with: {message}, is_sender: {is_sender}")

        # Obtener la hora actual
        current_time = QDateTime.currentDateTime().toString("HH:mm")

        font = QFont("Poppins", 10)
        item = QListWidgetItem()
        item_widget = QWidget()
        item_layout = QVBoxLayout(item_widget)  # Usar QVBoxLayout para la alineación vertical
        item_layout.setContentsMargins(10, 10, 10, 10)

        # Crear el mensaje con la hora
        message_text = QLabel(f"{message}")
        if is_sender:
            # Estilos para mensajes enviados
            message_text.setStyleSheet("""
                        background-color: #3e3e3e;
                        color: white;
                        padding: 10px;
                        border-radius: 15px;
                        max-width: 600px;
                        word-wrap: break-word;
                        text-align: left;
                        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                    """)
        else:
            # Estilos para mensajes recibidos
            message_text.setStyleSheet("""
                            background-color: transparent;
                            color: white;
                            padding: 10px;
                            word-wrap: break-word;
                            text-align: left;
                            max-width: 600%;
                        """)
        message_text.setFont(font)
        message_text.setWordWrap(True)  # Habilitar el ajuste de línea

        # Aplicar un efecto de sombra directamente al QLabel
        if is_sender:
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
        print("Adding item to chatHistory.")
        self.ui.chatHistory.addItem(item)
        self.ui.chatHistory.setItemWidget(item, item_widget)
        print("Item added to chatHistory.")
