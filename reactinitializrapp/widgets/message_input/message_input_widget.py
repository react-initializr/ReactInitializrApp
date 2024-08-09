from PySide6.QtWidgets import QWidget
from reactinitializrapp.widgets.message_input.ui_message_input_widget import Ui_MessageInputWidget


class MessageInputWidget(QWidget):
    def __init__(self, parent=None):
        super(MessageInputWidget, self).__init__(parent)
        self.ui = Ui_MessageInputWidget()
        self.ui.setupUi(self)

        # Conectar el botón de envío al método de envío
        self.ui.sendButton.clicked.connect(self.on_send_message)
        self.ui.messageInput.returnPressed.connect(self.on_send_message)

    def on_send_message(self):
        message = self.ui.messageInput.text()
        if message:
            self.parent().send_message(message)
            self.ui.messageInput.clear()
