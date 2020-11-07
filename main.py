import sys
import PySide2

from PySide2.QtWidgets import QApplication, QPushButton, QVBoxLayout, QDialog, QLineEdit
from PySide2.QtQuick import QQuickView
from PySide2.QtCore import Slot, QFile, QIODevice
from PySide2.QtUiTools import QUiLoader

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

    # view = QQuickView()
    # url = URL_Class()
    # view.setResizeMode(QQuickView.SizeRootObjectToView)
    # url.resize(800, 600)

    ui_file = "url_gui.ui"

    ui = QFile(ui_file)

    if not ui.open(QIODevice.ReadOnly):
        print (f"Cannot open {ui}: {ui.errorString()}")
        sys.exit(1)

    ui_loader = QUiLoader()
    window_loader = ui_loader.load(ui)
    ui.close()

    if not window_loader:
        print (ui_loader.errorString())
        sys.exit(1)

    window_loader.show()

    #url.show()

    sys.exit(app.exec_())