import sys
import os
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

import file_opener
import finder_7_1_w

home = str(Path.home())
first_char = len(home)
dir_list = os.listdir(home)

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        #self.cur_dir = home
        self.cur_dir = ''
        self.cur_word = None
        self.search_button = QPushButton('Search')
        self.ok_button = QPushButton('Ok')

        self.clicked_search = False
        self.search_button.clicked.connect(self.search_btn_clicked)

        # self.exit_button = QPushButton('Exit')
        # self.exit_button.setCheckable(True)
        # self.exit_button.toggle()
        # self.exit_button.clicked.connect(lambda: self.whichbtn(self.exit_button))
        #self.exit_button.clicked.connect(self.btnstate)

        self.searchEdit = QLineEdit()

        self.listwidget = QListWidget()

        self.listwidget.setFixedSize(1100, 400)
        self.listwidget.itemClicked.connect(self.btn_ok_result)


        # icon_folder = QtGui.QIcon('folder-icon.png')
        # item = QListWidgetItem(icon_folder, 'Hello World')
        # self.listwidget.addItem(item)
        # #list_of_words = ['Lean', 'Mean', 'Hacking', 'Machine']
        #
        # icon_drive = QtGui.QIcon('hard-drive-disk-icon.png')
        # item = QListWidgetItem(icon_drive, 'C:/ Drive')
        # self.listwidget.addItem(item)


        # for item in os.listdir(home):
        #     item = os.path.join(home, item)
        #     #print(item)
        #     if os.path.isfile(item):
        #         icon = QtGui.QIcon('hard-drive-disk-icon.png')
        #         # filename = item.strip(home)
        #         # print(filename)
        #         # name = QListWidgetItem(icon, filename)
        #         name = QListWidgetItem(icon, item[first_char+1:])
        #         # name = QListWidgetItem(icon, item)
        #         self.listwidget.addItem(name)
        #         #print(item + " is a file")
        #     elif os.path.isdir(item):
        #         icon = QtGui.QIcon('folder-icon.png')
        #         # filename = item.strip(home)
        #         # print(filename)
        #         # name = QListWidgetItem(icon, filename)
        #         name = QListWidgetItem(icon, item[first_char + 1:])
        #         # name = QListWidgetItem(icon, item)
        #         #name = QListWidgetItem(icon, item)
        #         self.listwidget.addItem(name)
        #         #print(item + " is a dir")
        #     else:
        #         icon = QtGui.QIcon('hard-drive-disk-icon.png')
        #         # filename = item.strip(home)
        #         # print(filename)
        #         # name = QListWidgetItem(icon, filename)
        #         name = QListWidgetItem(icon, item[first_char + 1:])
        #         # name = QListWidgetItem(icon, item)
        #         self.listwidget.addItem(name)
        #         #print("Unknown!")


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

    def search_btn_clicked(self, text_input):
        self.clicked_search = True
        sender = self.sender()
        words = self.searchEdit.text()
        self.cur_word = words

        list_of_search_results = finder_7_1_w.finder_result(words)

        self.listwidget.clear()

        for item in list_of_search_results:
            item = os.path.join(self.cur_dir, item)
            print(item)
            if os.path.isfile(item):
                icon = QtGui.QIcon('hard-drive-disk-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            elif os.path.isdir(item):
                icon = QtGui.QIcon('folder-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            else:
                icon = QtGui.QIcon('hard-drive-disk-icon.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''



    def btn_ok_result(self, file):
        print(file.text())
        print(self.clicked_search)

        if self.clicked_search is not False:
            print(self.clicked_search)
            print(self.cur_word)
            if file.text()[-4:] == 'xlsx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'docx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'pptx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return

        if file.text()[-4:] == 'xlsx':
            path = self.cur_dir + "\\" + file.text()
            file_opener.open_file(r'{}'.format(path), 'Hello')
            return
        elif file.text()[-4:] == 'docx':
            path = self.cur_dir + "\\" + file.text()
            file_opener.open_file(r'{}'.format(path), 'Hello')
            return
        elif file.text()[-4:] == 'pptx':
            path = self.cur_dir + "\\" + file.text()
            file_opener.open_file(r'{}'.format(path), 'Hello')
            return

        # print(file.text())
        # self.cur_dir = self.cur_dir + "\\" + file.text()
        # print(self.cur_dir)
        # first_char = len(self.cur_dir)


        # if self.cur_dir[-4:] == 'xlsx':
        #     print(self.cur_dir[-4:])
        #     #file_opener.open_file(r'C:\Users\chris\PycharmProjects\Testing.xlsx', 'Hello')
        #     file_opener.open_file(r'{}'.format(self.cur_dir), 'Hello')
        #     return
        # elif self.cur_dir[-4:] == 'docx':
        #     file_opener.open_file(r'{}'.format(self.cur_dir), 'Hello')
        #     return
        # elif self.cur_dir[-4:] == 'pptx':
        #     file_opener.open_file(r'{}'.format(self.cur_dir), 'Hello')
        #     return

        #self.listwidget.clear()


        # for item in os.listdir(self.cur_dir):
        #     item = os.path.join(self.cur_dir, item)
        #     if os.path.isfile(item):
        #         icon = QtGui.QIcon('hard-drive-disk-icon.png')
        #         name = QListWidgetItem(icon, item[first_char + 1:])
        #         self.listwidget.addItem(name)
        #     elif os.path.isdir(item):
        #         icon = QtGui.QIcon('folder-icon.png')
        #         name = QListWidgetItem(icon, item[first_char + 1:])
        #         self.listwidget.addItem(name)
        #     else:
        #         icon = QtGui.QIcon('hard-drive-disk-icon.png')
        #         name = QListWidgetItem(icon, item[first_char + 1:])
        #         self.listwidget.addItem(name)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    # w.show()
    sys.exit(app.exec_())
