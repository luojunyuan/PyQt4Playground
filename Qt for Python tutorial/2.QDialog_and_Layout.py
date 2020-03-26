from qtpy.QtCore import *
from qtpy.QtWidgets import *
from qtpy.QtGui import *


class Form(QDialog):

    def __init__(self, parent=None):
        # ~~I don't know the difference of these three~~
        # just use python3 grammar is OK
        # super().__init__(parent)
        # X this is wrong ~~super(QDialog, self).__init__(parent)~~
        # used by PySide tutorials
        super(Form, self).__init__(parent)
        self.setWindowTitle(self.tr("This is QDialog"))

        # no self is also OK
        # but most time, we will use method in those Widget, so self make it class globally
        self.edit = QLineEdit("Write my name here..")
        button = QPushButton("Show Greetings")
        button.clicked.connect(self.greetings)
        # vertically
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(button)
        # set dialog layout?
        self.setLayout(layout)
        # set a widgets with layout, use setLayout for QDialog

    def greetings(self):
        print(f"Hello {self.edit.text()}")


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec_())
