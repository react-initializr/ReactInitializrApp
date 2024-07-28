from PySide6.QtWidgets import QWidget


def apply_styles(widget: QWidget, qss_file_path: str):
    """
    Aplica estilos desde un archivo QSS a un widget.

    :param widget: El widget al que se aplicarán los estilos.
    :param qss_file_path: La ruta al archivo QSS.
    """
    try:
        with open(qss_file_path, "r") as file:
            qss = file.read()
            widget.setStyleSheet(qss)
    except Exception as e:
        print(f"Error al aplicar estilos desde {qss_file_path}: {e}")
