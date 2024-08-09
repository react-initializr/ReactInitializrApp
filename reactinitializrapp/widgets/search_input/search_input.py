from PySide6 import QtWidgets

from reactinitializrapp.widgets.search_input.ui_search_input import UISearchInput


class SearchInput(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SearchInput")
        self.ui = UISearchInput(self)
