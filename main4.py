import sys
import os

import datetime
from pathlib import Path
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
import file_opener
import finder_7_1_w

home = str(Path.home())
first_char = len(home)
dir_list = os.listdir(home)

found1 = True
globReady = False
while (found1):
    finder_7_1_w.creat()
    found1 = False
    globReady = True

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.UI()

    def UI(self):
        #self.cur_dir = home
        self.cur_dir = ''
        self.cur_word = None
        self.search_button = QPushButton('Search')
        self.exit_button = QPushButton('Exit')
        self.refresh_button = QPushButton('Refresh')

        self.groupbox = QGroupBox('Instructions')

        instruction1 = QLabel('1. Enter word(s) in text box.')
        instruction2 = QLabel('2. Click on Search Button.')
        instruction3 = QLabel('3. Double click on a file.')

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(instruction1)
        self.vbox.addWidget(instruction2)
        self.vbox.addWidget(instruction3)
        self.groupbox.setLayout(self.vbox)


        self.clicked_search = False
        self.search_button.clicked.connect(self.search_btn_clicked)

        self.refresh_button.clicked.connect(self.refresh_btn_clicked)

        self.exit_button.clicked.connect(self.close)

        self.searchEdit = QLineEdit()

        self.listwidget = QListWidget()

        self.listwidget.setFixedSize(1100, 400)
        self.listwidget.itemDoubleClicked.connect(self.btn_ok_result)



        layout = QGridLayout()
        layout.setSpacing(10)
        layout.addWidget(self.searchEdit, 1, 0)
        layout.addWidget(self.search_button, 1, 1)
        layout.addWidget(self.listwidget, 2, 0, 1, 6)
        layout.addWidget(self.exit_button, 6, 3)
        layout.addWidget(self.refresh_button, 6, 2)
        layout.addWidget(self.groupbox, 6, 0)
        #layout.addWidget(self.exit_button, 6, 2)


        self.setLayout(layout)
        self.setGeometry(300, 200, 1100, 700)
        self.show()

    def search_btn_clicked(self, text_input):
        self.clicked_search = True
        sender = self.sender()
        words = self.searchEdit.text()
        self.cur_word = words
        if(globReady == True):
            list_of_search_results = finder_7_1_w.searchDomain(words)

        self.listwidget.clear()

        for item in list_of_search_results:
            item = os.path.join(self.cur_dir, item)
            if item[-4:] == 'xlsx':
                icon = QtGui.QIcon('xl.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            elif item[-4:] == 'docx':
                icon = QtGui.QIcon('wd.jpg')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            elif item[-4:] == 'pptx':
                icon = QtGui.QIcon('pp.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''
            else:
                icon = QtGui.QIcon('pp.png')
                name = QListWidgetItem(icon, item)
                self.listwidget.addItem(name)
                self.cur_dir = ''


### Highliter
    def btn_ok_result(self, file):

        if self.clicked_search is not False:
            if file.text()[-4:] == 'xlsx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'docx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == 'pptx':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return
            elif file.text()[-4:] == '.txt':
                file_opener.open_file(r'{}'.format(file.text()), self.cur_word)
                return


    def refresh_btn_clicked(self):
        finder_7_1_w.creat()
        self.listwidget.clear()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    # w.show()
    sys.exit(app.exec_())
