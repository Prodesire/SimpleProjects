# coding:utf-8
import os
from subprocess import Popen
from PyQt5.QtWidgets import QPushButton

# Basic custom button which set size of button
class CustomButton(QPushButton):
    def __init__(self, title):
        QPushButton.__init__(self, title)
        self.setFixedSize(130, 80)


class OpenButton(CustomButton):
    def __init__(self, title, app_path):
        CustomButton.__init__(self, title)
        self.app_path = app_path
        self.clicked.connect(self.open_app)

    def open_app(self):
        os.chdir(os.path.dirname(self.app_path))
        os.startfile(self.app_path)


class EditButton(CustomButton):
    def __init__(self, title, app_path, editfrom, editto):
        CustomButton.__init__(self, title)
        self.app_path = app_path
        self.editfrom, self.editto = editfrom, editto
        self.clicked.connect(self.edit_app)

    def edit_app(self):
        with open(self.app_path, 'r', encoding='utf-8') as app:
            content = app.read().replace(self.editfrom, self.editto)
        with open(self.app_path, 'w', encoding='utf-8') as app:
            app.write(content)


class CmdButton(CustomButton):
    def __init__(self, title, cmd):
        CustomButton.__init__(self, title)
        self.cmd = cmd
        self.clicked.connect(self.execute_cmd)

    def execute_cmd(self):
        Popen(self.cmd)