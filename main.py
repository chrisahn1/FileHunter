import sys
import os
from pathlib import Path
#from PyQt5.QtWidgets import (QPushButton, QLineEdit, QInputDialog, QApplication, QWidget)
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

print(os.getlogin())
home = str(Path.home())
#path = os.getcwd()
dir_list = os.listdir(home)
print(home)
print(dir_list)

# path = str(Path.home())
# for item in os.listdir(path):
#     item = os.path.join(path, item)
#     if os.path.isfile(item):
#         print(item + " is a file")
#     elif os.path.isdir(item):
#         print(item + " is a dir")
#     else:
#         print("Unknown!")



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        self.search_button = QPushButton('Search')
        self.ok_button = QPushButton('Ok')
        #self.ok_button.setCheckable(True)
        #self.ok_button.toggle()
        #self.ok_button.clicked.connect(lambda: self.whichbtn(self.ok_button))
        self.ok_button.clicked.connect(self.btn_ok)

        # self.exit_button = QPushButton('Exit')
        # self.exit_button.setCheckable(True)
        # self.exit_button.toggle()
        # self.exit_button.clicked.connect(lambda: self.whichbtn(self.exit_button))
        #self.exit_button.clicked.connect(self.btnstate)

        self.searchEdit = QLineEdit()

        self.listwidget = QListWidget()

        #self.listwidget = QListView()
        #self.listwidget.setViewMode(QListView.IconMode)
        #self.listwidget.setGeometry(QtCore.QRect(120, 10, 281, 192))
        self.listwidget.setFixedSize(1100, 400)
        self.listwidget.itemClicked.connect(self.btn_ok_result)


        icon_folder = QtGui.QIcon('folder-icon.png')
        item = QListWidgetItem(icon_folder, 'Hello World')
        self.listwidget.addItem(item)
        #list_of_words = ['Lean', 'Mean', 'Hacking', 'Machine']

        icon_drive = QtGui.QIcon('hard-drive-disk-icon.png')
        item = QListWidgetItem(icon_drive, 'C:/ Drive')
        self.listwidget.addItem(item)

        for item in os.listdir(home):
            item = os.path.join(home, item)
            if os.path.isfile(item):
                icon = QtGui.QIcon('hard-drive-disk-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                #print(item + " is a file")
            elif os.path.isdir(item):
                icon = QtGui.QIcon('folder-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                #print(item + " is a dir")
            else:
                print("Unknown!")


        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(self.searchEdit, 1, 0)
        layout.addWidget(self.search_button, 1, 1)
        layout.addWidget(self.listwidget, 2, 0, 1, 6)
        layout.addWidget(self.ok_button, 6, 1)
        #layout.addWidget(self.exit_button, 6, 2)


        self.setLayout(layout)
        self.setGeometry(300, 200, 1100, 700)
        self.show()

    def btn_ok(self):
        print('Hello World')



    def btn_ok_result(self, file):
        #print('click -> {}'.format(file.text()))
        print(file.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    # w.show()
    sys.exit(app.exec_())







