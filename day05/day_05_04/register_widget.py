'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

from PyQt5.QtWidgets import *
from PyQt5.Qt import QFont
from PyQt5.QtCore import pyqtSignal
from pymysql import connect

class RegisterWidget(QWidget):
    register_success = pyqtSignal()

    def __init__(self):
        super(RegisterWidget, self).__init__()

        hbox = QHBoxLayout(self)
        hbox.addStretch()

        vbox = QVBoxLayout()
        label = QLabel("学生管理系统")
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        label.setFont(font)
        vbox.addWidget(label)
        hbox.addWidget(vbox)

        form_layout = QFormLayout()

        self.username_edit = QLineEdit()
        form_layout.addRow("用户名：", self.username_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addRow("密码：", self.password_edit)

        self.nickname_edit = QLineEdit()
        form_layout.addRow("昵称：", self.nickname_edit)

        register_btn = QPushButton("注册")
        register_btn.clicked.connect(self.register)
        form_layout.addRow("", register_btn)

        vbox.addWidget(form_layout)
        hbox.addStretch()

    def register(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        nickname = self.nickname_edit.text()

        conn = connect(host="localhost", port=3306, user="admin", password="123456")
        sql = "insert into user values(null, %s, %s, %s)"
        cursor = conn.cursor()
        ret = cursor.execute(sql, [username, password, nickname])
        conn.commit()

        if ret == 1:
            print("注册成功")
            QMessageBox.information(None, '提示', '恭喜你， 注册成功！')
            self.register_success.emit();
        else:
            print("注册失败！")

        cursor.close()
        conn.close()