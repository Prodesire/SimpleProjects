# coding:utf-8
import sys, os
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QDesktopWidget, QMainWindow, \
    QLabel, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon

from Shortcut.configloader import ConfigLoader, ConfigError
from Shortcut.button import OpenButton, EditButton, CmdButton


class ShortcutWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setWindowTitle('Shortcut')
        self.setWindowIcon(QIcon(os.path.join(os.curdir, 'icons/Shortcut.ico')))
        self.resize(300, 400)
        screenRect = QDesktopWidget().screenGeometry()
        self.move((screenRect.width() - self.width()) / 2, (screenRect.height() - self.height()) / 2)

        self.mainWidget = QWidget()
        self.gridlayout = QGridLayout()
        self.mainWidget.setLayout(self.gridlayout)
        self.setCentralWidget(self.mainWidget)

        try:
            configloader = ConfigLoader()
        except ConfigError as e:
            QMessageBox.about(self, 'Config Error', str(e))
            return

        for i, (title, action) in enumerate(configloader.config.items()):
            if 'open' in action[0]:
                button = OpenButton(title, action[1])
            elif 'edit' in action[0]:
                button = EditButton(title, action[1], action[2])
            elif 'cmd' in action[0]:
                button = CmdButton(title, action[1])
            else:
                continue

            colnum = 2
            self.gridlayout.addWidget(button, i / colnum, i % colnum)


app = QApplication(sys.argv)
window = ShortcutWindow()
window.show()
sys.exit(app.exec())
