import sys

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

# 在Qt中每一个model类最少要实现两个方法，rowCount() and data()

# original code file here: http://www.yasinuludag.com/PyQt/Tutorial02/Tutorial02_ListModel.py

# i just mix the Qt5 and Qt4...
# from PyQt5.QtCore import QAbstractListModel


class PalletListModel(QAbstractListModel):

    def __init__(self, colors=None, parent=None):
        super().__init__(parent)
        if colors is None:
            colors = []
        self.__colors = colors

    def rowCount(self, parent=None, **kwargs):
        # 因为不是树形结构，所以parent暂且用不上
        return len(self.__colors)

    def data(self, index, role=None):

        # if role == Qt.EditRole:
        #     return self.__colors[index.row()].name()

        # if role == Qt.ToolTipRole:
        #     return "Hex code: " + self.__colors[index.row()].name()

        if role == Qt.DecorationRole:
            row = index.row()
            value = self.__colors[row]

            pixmap = QPixmap(26, 26)
            pixmap.fill(value)

            icon = QIcon(pixmap)

            return icon

        if role == Qt.DisplayRole:
            row = index.row()
            value = self.__colors[row]

            return value


if __name__ == '__main__':
    app = QApplication([])

    red = QColor(255, 0, 0)
    green = QColor(0, 255, 0)
    blue = QColor(0, 0, 255)

    data = [red, green, blue]
    # 1.这边的model不需要设置parent?
    model = PalletListModel(data)
    # 2.还是因为是tableView的关系
    view = QTableView()
    view.setModel(model)
    view.show()

    sys.exit(app.exec_())
