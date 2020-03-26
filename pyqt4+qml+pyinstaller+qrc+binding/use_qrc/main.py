import sys
import os
os.environ['QT_API'] = 'PyQt4'
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from PyQt4.QtDeclarative import QDeclarativeView

import resource
# import PyQt4.QtNetwork

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller 
    http://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        # 打包后走这边
        print(sys._MEIPASS)
        base_path = sys._MEIPASS
    except Exception:
        # dev时走这边
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
 
if __name__ == '__main__':
    app = QApplication([])

    view = QDeclarativeView()
    # 这里相当于传进的成绝对路径了
    # path = 'file:///' + resource_path('view.qml')
    # view.setSource(QUrl(path))
    view.setSource(QUrl('qrc:view.qml'))
    # dev的时候resource_path 就setSource到当前目录下文件了
    # 打包完过后 就setSource到那个TMP目录下的文件去了
    # 相当于我之前打包的时候，在spec文件中写入了文件，运行时文件才会跑到TMP里去了的
    view.setAttribute(Qt.WA_TranslucentBackground)

    view.setStyleSheet("background-color:transparent")
    view.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
    view.showFullScreen()

    app.exec_()
