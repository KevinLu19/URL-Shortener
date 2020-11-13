from url_gui_file import Ui_MainWindow
from shorten_url import URL_DB_Class

from PyQt5 import QtCore, QtGui, QtWidgets

import sys

# url_gui_file.py generated via command
# pyuic5 -x <.ui file> -o <output_file.py>

class MainFileClass(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainFileClass, self).__init__()
        self.setupUi(self)
        self.short_url_button.clicked.connect(self.temporary_button)

    def temporary_button(self):
        print ("Temproary button function connection.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainFileClass()
    db_class = URL_DB_Class()

    ui.show()
    sys.exit(app.exec_())