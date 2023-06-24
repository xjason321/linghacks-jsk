"""
LING HACKS V 

Idea:
Description:

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""


from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LingHacks V Project")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()

