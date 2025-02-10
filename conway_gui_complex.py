from PyQt6.QtWidgets import (
    QGridLayout, QFormLayout, QApplication, QGroupBox, QWidget, QLineEdit,
    QPushButton, QLabel, QMessageBox
)
from PyQt6.QtGui import QIcon, QIntValidator
import sys
import time

class ConwayComplex(QWidget):
    def __init__(self):
        super().__init__()

        self.generations = 0

        self.setWindowTitle("Complex Conway's Game of Life")
        self.setWindowIcon(QIcon('infinity.png'))

        self.label_gen = QLabel("Generation:")

        self.layout = QFormLayout(self)
        self.setLayout(self.layout)

        self.ln_rows_complex = QLineEdit()
        self.ln_cols_complex = QLineEdit()
        self.ln_gen_complex = QLineEdit()

        validator = QIntValidator(1, 50)
        self.ln_rows_complex.setValidator(validator)
        self.ln_cols_complex.setValidator(validator)
        self.ln_gen_complex.setValidator(QIntValidator())

        self.ln_rows_complex.textChanged.connect(lambda: self.validate_range(self.ln_rows_complex))
        self.ln_cols_complex.textChanged.connect(lambda: self.validate_range(self.ln_cols_complex))

        self.button_dibujar_matrix = QPushButton("Draw Matrix", self)
        self.button_dibujar_matrix.clicked.connect(self.draw_matrix)

        self.button_stop = QPushButton("Stop Game", self)
        self.button_stop.clicked.connect(self.stop_game)

        self.button_start = QPushButton("Start Game", self)
        self.button_start.clicked.connect(self.start_game)

        # Grupo de controles
        self.gBoxComplexPlay = QGroupBox("Complex Game Mode")
        self.form_layout = QFormLayout()

        
        self.gBoxComplexPlay.setLayout(self.form_layout)

        self.form_layout.addRow(self.label_gen)
        self.form_layout.addRow("Rows:", self.ln_rows_complex)
        self.form_layout.addRow("Cols:", self.ln_cols_complex)
        self.form_layout.addRow("Generations:", self.ln_gen_complex)
        self.form_layout.addWidget(self.button_dibujar_matrix)
        self.form_layout.addWidget(self.button_start)
        self.form_layout.addWidget(self.button_stop)

        self.layout.addWidget(self.gBoxComplexPlay)

        # Layout de la cuadrícula
        self.layoutx = QGridLayout()
        self.layoutx.setVerticalSpacing(0)
        self.layoutx.setHorizontalSpacing(0)
        self.form_layout.addRow(self.layoutx)

        self.grid = []
        self.rows = 0
        self.cols = 0

    def stop_game(self):
        self.generations=-1

    def validate_range(self, line_edit):
        texto = line_edit.text()

        if texto: 
            valor = int(texto)

            if valor < 1:
                line_edit.setText("1")  
            elif valor > 50:
                line_edit.setText("50") 

    def draw_matrix(self):
        """Draw Game Field."""
        try:
            
            self.label_gen.setText("Generation:")
            self.rows = int(self.ln_rows_complex.text())
            self.cols = int(self.ln_cols_complex.text())
        except ValueError:
            QMessageBox.critical(self, "Error", "Rows and Columns must be valid numbers.")
            return

        # Limpiar cuadrícula
        while self.layoutx.count():
            item = self.layoutx.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.grid = [[0] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                btn = QPushButton("")
                btn.setFixedSize(10, 10)
                btn.setStyleSheet("background-color: white; border: 1px solid black;")
                btn.clicked.connect(lambda _, r=i, c=j: self.toggle_cell(r, c))
                self.layoutx.addWidget(btn, i, j)

    def toggle_cell(self, r, c):
        """Enables or disables a cell."""
        self.grid[r][c] = 1 - self.grid[r][c]  # Switch 0 or 1
        btn = self.layoutx.itemAtPosition(r, c).widget()

        if self.grid[r][c] == 1:
            btn.setStyleSheet("background-color: black; border: 1px solid black;")  # Alive
        else:
            btn.setStyleSheet("background-color: white; border: 1px solid black;")  # Dead

    def start_game(self):
        """Begins game!."""
        try:
            self.generations = int(self.ln_gen_complex.text())

            if  self.generations <= 0:
                raise ValueError("Generations must be greater than 0.")

            for x in range( self.generations):
                if  self.generations == -1:
                    raise ValueError("Conway is stopped!")

                self.label_gen.setText('Current Generation: '+str( self.generations) + '/' + str(x+1))
                self.update_grid()
                QApplication.processEvents()
                time.sleep(0.1)  # Refresh Rate

        except ValueError as e:
            QMessageBox.critical(self, "Error", str(e))

    def update_grid(self):
        """Conway rule and update."""
        new_grid = [[0] * self.cols for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(i, j)

                if self.grid[i][j] == 1:
                    if alive_neighbors in [2, 3]:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbors == 3:
                        new_grid[i][j] = 1

        self.grid = new_grid
        self.update_buttons()
        self.check_stop()

    def check_stop(self):
        flag = False
        for i in range(self.rows):
            for j in range(self.cols):
                if flag is False:
                    flag = self.grid[i][j] == 1
                            
        if flag is False:
            self.generations= -1

    def count_alive_neighbors(self, x, y):
        """Count alive neighbours."""
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == 1:
                count += 1

        return count

    def update_buttons(self):
        """Refresh UI."""
        for i in range(self.rows):
            for j in range(self.cols):
                btn = self.layoutx.itemAtPosition(i, j).widget()
                if self.grid[i][j] == 1:
                    btn.setStyleSheet("background-color: black; border: 1px solid black;")
                else:
                    btn.setStyleSheet("background-color: white; border: 1px solid black;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConwayComplex()
    window.show()
    sys.exit(app.exec())
