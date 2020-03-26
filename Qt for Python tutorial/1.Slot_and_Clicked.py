import sys
from qtpy.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from qtpy.QtCore import Slot
from PyQt5.QtWidgets import QPushButton

@Slot()
def say_hello():
    print("hello world")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("<font color=red size=40>Hello World!</font>")
    button = QPushButton('Click me!')
    button.clicked.connect(say_hello)
    label.show()
    button.show()

    sys.exit(app.exec_())
