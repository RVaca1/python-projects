import sys
from PySide6.QtWidgets import QApplication, QPushButton

def function():
    print("The 'function' has been called!")


app = QApplication()
button = QPushButton("Call function")

button.clicked.connect(say_hello)

button.show()

:QPushButton
