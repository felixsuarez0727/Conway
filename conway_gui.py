from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QDialog,QDialogButtonBox
from PyQt6.QtGui import QIcon, QIntValidator
from PyQt6.QtCore import QThread
from custom_dialog import CustomDialog
from worker import Worker  # Asumiendo que Worker está en un archivo separado
import sys
class NumeroInput(QWidget):
    def __init__(self):
        super().__init__()
        self.count = 0

        # Configura la ventana principal
        self.setWindowTitle("Conway's Game of Life")
        self.setWindowIcon(QIcon('infinity.png'))
        self.setFixedWidth(400)

        # Crea los labels y los campos de entrada
        self.label1 = QLabel("Rows:")
        self.ln_rows = QLineEdit()
        self.ln_rows.setValidator(QIntValidator())
        self.label2 = QLabel("Columns:")
        self.ln_cols = QLineEdit()
        self.ln_cols.setValidator(QIntValidator())
        self.label3 = QLabel("Generations:")
        self.ln_gen = QLineEdit()
        self.ln_gen.setValidator(QIntValidator())
        self.label4 = QLabel("Probability Percentage:")
        self.ln_prob = QLineEdit()
        self.ln_prob.setValidator(QIntValidator())

        self.button_start = QPushButton("&Start Game", self)
        self.button_start.clicked.connect(self.start_game)

        # Crea un layout vertical para organizar los elementos
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.ln_rows)
        layout.addWidget(self.label2)
        layout.addWidget(self.ln_cols)
        layout.addWidget(self.label3)
        layout.addWidget(self.ln_gen)
        layout.addWidget(self.label4)
        layout.addWidget(self.ln_prob)
        layout.addWidget(self.button_start)
        self.setLayout(layout)

    def start_game(self):
        try:
            if not self.ln_rows.text().strip() or not self.ln_cols.text().strip() or not self.ln_gen.text().strip() or not self.ln_prob.text().strip():
                raise ValueError("All the fields are mandatory.")

            rows = int(self.ln_rows.text().strip())
            cols = int(self.ln_cols.text().strip())
            gen = int(self.ln_gen.text().strip())
            prob = int(self.ln_prob.text().strip())

             

            if rows <= 0 or cols <= 0 or gen <= 0:
                raise ValueError("Rows, Columns y Generations must be more than 0.")
            if prob < 0 or prob > 100:
                raise ValueError("Probability must be between 0 and 100 (inclusive).")

            
            self.worker = Worker(rows, cols, gen, prob / 100)
            self.worker.animation_ready.connect(self.show_animation)
            self.worker.error.connect(self.on_game_error)
            self.worker.start()

        except ValueError as ve:
            dialog = CustomDialog("Error", str(ve))
            dialog.exec()
        except Exception as err:
            dialog = CustomDialog("Unexpected Error", str(err))
            dialog.exec()

    def show_animation(self, con):     
        con.main()

    def on_game_error(self, error_message):
        dialog = CustomDialog("Error", error_message)
        dialog.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NumeroInput()
    window.show()
    sys.exit(app.exec())