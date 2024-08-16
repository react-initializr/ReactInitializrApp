from PySide6.QtCore import QThread, Signal

class ApiThread(QThread):
    result_signal = Signal(str)
    error_signal = Signal(str)

    def __init__(self, client, model, messages):
        super(ApiThread, self).__init__()
        self.client = client
        self.model = model
        self.messages = messages

    def run(self):
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.5,
                max_tokens=600
            )
            content = response.choices[0].message.content
            self.result_signal.emit(content)
        except Exception as e:
            self.error_signal.emit(str(e))