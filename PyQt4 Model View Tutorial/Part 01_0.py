from PyQt4 import QtGui, QtCore, uic
import sys

# 注意在这个例子中，修改一个数据所有的view中的数据都会跟着改变！！！！

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    # DATA
    data = ["one", "two", "three", "four", "five"]

    # 如果不给model设置一个父类就会有如下报错
    # Object::startTimer: QTimer can only be used with threads started with QThread
    model = QtGui.QStringListModel(data)  # 这个父类添加到第二个参数，应该是要设置为一个view的

    listView = QtGui.QListView()
    listView.setModel(model)
    listView.show()

    # 上述的报错似乎对QComboBox没有影响
    combobox = QtGui.QComboBox()
    combobox.setModel(model)
    combobox.show()

    listView2 = QtGui.QListView()
    listView2.show()
    listView2.setModel(model)

    sys.exit(app.exec_())
