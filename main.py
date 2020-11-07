import sys
import PySide2

from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QDialog, QLineEdit
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import Slot
from PySide2.QtCore import QFile

class URL_Class(QDialog):
    def __init__(self, parent=None):
        super(URL_Class, self).__init__(parent)

        self.setWindowTitle("URL Shortener")

        self.edit = QLineEdit("Enter URL")
        self.button = QPushButton("Shortening URL")

        layout_container = QVBoxLayout()
        layout_container.addWidget(self.edit)
        layout_container.addWidget(self.button)

        self.setLayout(layout_container)

        self.button.clicked.connect(self.short_url)

    def short_url(self):
        print ("Button connected")
        return True

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QQuickView()
    url = URL_Class()
    view.setResizeMode(QQuickView.SizeRootObjectToView)
    url.resize(800, 600)
    ui = QFile("url_gui.ui")

    url.show()

    sys.exit(app.exec_())