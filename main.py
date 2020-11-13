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
        self.short_url_button.clicked.connect(self.send_user_url)
        self.setWindowTitle("Short That URL")
        self.__url_db = URL_DB_Class()

    def send_user_url (self):
        qt_url_text_edit = self.url_input_text.toPlainText()
        self.__url_db.set_original_user_url(qt_url_text_edit)

    # def temporary_button(self):
    #     print ("Temproary button function connection.")
    #     print ("stuff that's stores textedit: %s" % self.url_input_text.toPlainText())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainFileClass()
    ui.show()
    sys.exit(app.exec_())