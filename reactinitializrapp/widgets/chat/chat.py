# chat.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from reactinitializrapp.widgets.chat.ui_chat import Ui_ChatWidget
from reactinitializrapp.widgets.messages.messages_widget import MessagesWidget
from reactinitializrapp.widgets.message_input.message_input_widget import MessageInputWidget
from openai import OpenAI
from dotenv import load_dotenv
from PySide6.QtGui import QFont, QFontDatabase
import os


class ChatWidget(QWidget):
    def __init__(self, parent):
        super(ChatWidget, self).__init__(parent)

        # Cargar las variables de entorno
        load_dotenv()

        # Configuración del cliente de OpenAI
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)

        # Modelo a utilizar
        self.modelo = 'gpt-3.5-turbo'
        self.mensajes = [
            {"role": "system",
             "content": "React Initializr es un modelo capaz de generar los comandos necesarios para la creación de proyectos React."}
        ]

        # Cargar la fuente personalizada
        QFontDatabase.addApplicationFont("assets/fonts/Poppins/Poppins-Regular.ttf")
        font = QFont("Poppins", 10)

        # Configuración del layout principal
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        # Inicializar los widgets
        self.messagesWidget = MessagesWidget(self)
        self.messageInputWidget = MessageInputWidget(self)

        # Agregar los widgets al layout
        self.verticalLayout.addWidget(self.messagesWidget)
        self.verticalLayout.addWidget(self.messageInputWidget)

        # Agregar un mensaje de prueba como si fuera recibido
        self.messagesWidget.add_message(
            "React Initializr es un modelo capaz de generar proyectos React preconfigurados.", is_sender=False)

    def send_message(self, message):
        if message:
            # Añadir el mensaje enviado al widget de mensajes
            self.messagesWidget.add_message(message, is_sender=True)

            # Enviar el mensaje a la API de OpenAI y obtener la respuesta
            self.mensajes.append({"role": "user", "content": message})
            response = self.client.chat.completions.create(
                model=self.modelo,
                messages=self.mensajes,
                temperature=0.5,
                max_tokens=600
            )

            # Obtener el contenido de la respuesta
            content = response.choices[0].message.content

            # Añadir la respuesta al widget de mensajes
            self.messagesWidget.add_message(content, is_sender=False)

            # Añadir la respuesta a la lista de mensajes para mantener el contexto
            self.mensajes.append({"role": "assistant", "content": content})
