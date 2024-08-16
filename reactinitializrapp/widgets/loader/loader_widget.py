from PySide6.QtWidgets import QWidget
from reactinitializrapp.widgets.loader.ui_loader_widget import Ui_LoaderWidget


class LoaderWidget(QWidget):
    def __init__(self, parent=None):
        super(LoaderWidget, self).__init__(parent)
        self.ui = Ui_LoaderWidget()
        self.ui.setupUi(self)

    def start_loading(self):
        # Iniciar la animación del loader
        self.ui.loader_movie.start()
        self.show()

    def stop_loading(self):
        # Detener la animación del loader
        self.ui.loader_movie.stop()
        self.hide()
