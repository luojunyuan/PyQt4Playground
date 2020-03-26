import sys

import os
# os.environ['QT_API'] = 'pyside'

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

# import resources

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        print('insert')
        QTimer.singleShot(0, self.test)
        QTimer().singleShot(0, self.test)
        print('insert2')

    def test(self):
        print('ssssssss')


if __name__ == '__main__':
    app = QApplication([])

    win = MainWindow()
    win.show()

    app.exec_()
