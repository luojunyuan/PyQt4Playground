import sys

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.items = 0

        # Example data
        self._data = {"Water": 24.5, "Electricity": 55.1, "Rent": 850.0,
                      "Supermarket": 230.4, "Internet": 29.99, "Bars": 21.85,
                      "Public transportation": 60.0, "Coffee": 22.45, "Restaurants": 120}

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Description", "Price"])
        # 拉伸content 用掉所有widget的空间
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.fill_table()

        # Right
        self.description = QLineEdit()
        self.price = QLineEdit()
        self.add = QPushButton("Add")
        self.clear = QPushButton("Clear")
        self.quit = QPushButton("Quit")

        self.right = QVBoxLayout()
        # self.right.setMargin(10)
        self.right.addWidget(QLabel("Description"))
        self.right.addWidget(self.description)
        self.right.addWidget(QLabel("Price"))
        self.right.addWidget(self.price)
        self.right.addWidget(self.add)
        self.right.addStretch()
        self.right.addWidget(self.clear)
        self.right.addWidget(self.quit)

        self.add.clicked.connect(self.add_element)
        self.quit.clicked.connect(self.quit_application)
        self.clear.clicked.connect(self.clear_table)

        # QWidget Layout
        self.layout = QHBoxLayout()

        #self.table_view.setSizePolicy(size)
        self.layout.addWidget(self.table)
        self.layout.addLayout(self.right)
        self.setLayout(self.layout)

    def fill_table(self, data=None):
        # 如果data有参数传进来有就用data，否则用self._data
        data = self._data if not data else data
        for desc, price in data.items():
            # description price
            # s设置几号位
            self.table.insertRow(self.items)
            #                  行row      列col
            self.table.setItem(self.items, 0, QTableWidgetItem(desc))
            self.table.setItem(self.items, 1, QTableWidgetItem(str(price)))
            self.items += 1  # increase

    @Slot()
    def add_element(self):
        # 获取字段中的文本
        des = self.description.text()
        price = self.price.text()

        # 插入新行
        self.table.insertRow(self.items)
        self.table.setItem(self.items, 0, QTableWidgetItem(des))
        self.table.setItem(self.items, 1, QTableWidgetItem(price))

        # 清除输入的文本
        self.description.setText("")
        self.price.setText("")

        self.items += 1

    @Slot()
    def quit_application(self):
        QApplication.quit()

    @Slot()
    def clear_table(self):
        # 将table清0 只需setRowCount
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, w=None):
        super().__init__()
        self.setWindowTitle("Tutorial")
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # 一个QAction 需要设置一个信号triggered
        exit_action = QAction("Exit", self)
        # This str must be series no space
        exit_action.setShortcut('Ctrl+Q')
        # exit_action.triggered.connect(lambda: QApplication.exit())  # what's the difference .quit()
        exit_action.triggered.connect(self.exit_app)


        self.file_menu.addAction(exit_action)

        self.setCentralWidget(w)

    @Slot()
    def exit_app(self):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication([])

    widget = Widget()

    # QMainWindow 可以设置一个中心的 widget父类，基类必须是widget继承而来
    win = MainWindow(widget)
    win.resize(800, 600)
    win.show()
    # widget.show() #this will make another window
    sys.exit(app.exec_())
