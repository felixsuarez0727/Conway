from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QIcon
import sys

class CustomDialog(QDialog):
    def __init__(self, title, content):
        super().__init__()
        self.title_msg = title
        self.content_msg = content

        # Set up the dialog
        self.setWindowTitle(self.title_msg)
        self.setWindowIcon(QIcon('infinity.png')) 

        # Add a label
        self.label = QLabel(self.content_msg)
         

        # Add a button
        self.button = QPushButton("Ok")
        self.button.clicked.connect(self.close_dialog)

        # Create and set a layout
        layout = QVBoxLayout()
        
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def close_dialog(self):
        self.accept()  # Closes the dialog and returns QDialog.Accepted