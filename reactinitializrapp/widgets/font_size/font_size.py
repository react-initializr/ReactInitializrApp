from PySide6 import QtWidgets

from reactinitializrapp.widgets.font_size.ui_font_size import UIFontSize


class FontSize(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UIFontSize(self)
