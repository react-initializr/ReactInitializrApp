# chat.py
from PySide6.QtWidgets import QWidget, QVBoxLayout

from reactinitializrapp.widgets.chat.api_thread import ApiThread
from reactinitializrapp.widgets.chat.ui_chat import Ui_ChatWidget
from reactinitializrapp.widgets.messages.messages_widget import MessagesWidget
from reactinitializrapp.widgets.message_input.message_input_widget import MessageInputWidget
from reactinitializrapp.widgets.loader.loader_widget import LoaderWidget
from openai import OpenAI
from dotenv import load_dotenv
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import QTimer, Qt
import threading
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
        self.loaderWidget = LoaderWidget(self)  # Asegúrate de inicializar el LoaderWidget aquí

        # Aplicar la fuente a los widgets
        self.messagesWidget.setFont(font)
        self.messageInputWidget.setFont(font)

        # Agregar los widgets al layout
        self.verticalLayout.addWidget(self.messagesWidget)
        self.verticalLayout.addWidget(self.loaderWidget)  # Añadir el LoaderWidget al layout
        self.verticalLayout.addWidget(self.messageInputWidget)

        # Ocultar el loader al inicio
        self.loaderWidget.hide()

        # Agregar un mensaje de prueba como si fuera recibido
        self.messagesWidget.add_message(
            "React Initializr es un modelo capaz de generar proyectos React preconfigurados.", is_sender=False)

    def send_message(self, message):
        if message:
            # Mostrar el loader mientras se espera la respuesta
            self.loaderWidget.start_loading()
            # Añadir el mensaje enviado al widget de mensajes
            self.messagesWidget.add_message(message, is_sender=True)



            # Enviar el mensaje a la API de OpenAI en un hilo separado
            self.mensajes.append({"role": "user", "content": message})
            # Crear y ejecutar el hilo para la API
            self.api_thread = ApiThread(self.client, self.modelo, self.mensajes)
            self.api_thread.result_signal.connect(self.handle_result)
            self.api_thread.error_signal.connect(self.handle_error)
            self.api_thread.start()

    def handle_result(self, content):
        # Añadir la respuesta al widget de mensajes
        self.messagesWidget.add_message(content, is_sender=False)

        # Añadir la respuesta al contexto para mantener la conversación
        self.mensajes.append({"role": "assistant", "content": content})

        # Ocultar el loader después de recibir la respuesta
        self.loaderWidget.stop_loading()

    def handle_error(self, error_message):
        # Manejar el error mostrando el mensaje en la UI
        self.messagesWidget.add_message(f"Error: {error_message}", is_sender=False)

        # Ocultar el loader en caso de error
        self.loaderWidget.stop_loading()