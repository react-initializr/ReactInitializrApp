# chat.py
from PySide6.QtWidgets import QWidget
from reactinitializrapp.widgets.chat.ui_chat import Ui_ChatWidget


class ChatWidget(QWidget):
    def __init__(self, parent):
        super(ChatWidget, self).__init__(parent)
        self.ui = Ui_ChatWidget()
        self.ui.setupUi(self)

        # Conectar el botón de envío al método de envío
        self.ui.sendButton.clicked.connect(self.send_message)
        # Agregar un mensaje de prueba como si fuera recibido
        self.ui.add_message("React Initializr es un modelo capaz de generar proyectos React preconfigurados.", is_sender=False)

    def send_message(self):
        message = self.ui.messageInput.text()
        if message:
            formatted_message = f'''
                <div style="
                    display: flex;
                    justify-content: flex-end;
                    margin: 5px 0;
                ">
                    <span style="
                        background-color: #007bff;
                        color: white;
                        padding: 10px;
                        border-radius: 10px;
                        word-wrap: break-word;
                    ">
                        {message}
                    </span>
                </div>
            '''
            self.ui.chatHistory.append(formatted_message)
            self.ui.messageInput.clear()
