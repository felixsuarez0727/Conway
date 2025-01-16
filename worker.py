from PyQt6.QtCore import QThread, pyqtSignal
from conway import Conway


class Worker(QThread):
    # Señal para notificar al hilo principal cuando la animación esté lista
    animation_ready = pyqtSignal(object)
    # Señal para manejar errores
    error = pyqtSignal(str)

    def __init__(self, rows, cols, gen, prob, parent=None):
        super().__init__(parent)
        self.rows = rows
        self.cols = cols
        self.gen = gen
        self.prob = prob
        self.con = None

    def run(self):
        try:
            # Crear la instancia de Conway y ejecutar el juego
            self.con = Conway(self.rows, self.cols, self.gen, self.prob)
            # Emitir la señal con el objeto de Conway
            self.animation_ready.emit(self.con)
        except Exception as e:
            # Emitir la señal de error
            self.error.emit(str(e))