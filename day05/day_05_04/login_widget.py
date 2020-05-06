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

class LoginWidget(QWidget):
    login_success = pyqtSignal()

    def __init__(self):
        super(LoginWidget, self).__init__()

        hbox = QHBoxLayout(self)
        hbox.addStretch()

        vbox = QVBoxLayout()
        label = QLabel("学生管理系统")
        font = QFont("微软雅黑", 30)
        font.setBold(True)
        label.setFont(font)
        vbox.addWidget(label)
        hbox.addLayout(vbox)

        form_layout = QFormLayout()

        self.username_edit = QLineEdit()
        form_layout.addRow("用户名：", self.username_edit)

        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addRow("密码：", self.password_edit)

        login_btn = QPushButton("登录")
        login_btn.clicked.connect(self.login)
        form_layout.addRow("", login_btn)

        vbox.addLayout(form_layout)
        hbox.addStretch()
        print("login inited.")

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        conn = connect(host="localhost", port=3306, user="admin", password="123456", database="itheima")
        sql = "select * from user where username=%s and password=%s;"
        cursor = conn.cursor()
        ret = cursor.execute(sql, [username, password])

        user = cursor.fetchone()

        if user:
            print("登录成功")
            QMessageBox.information(None, '提示', '恭喜你， 登录成功！')
            self.login_success.emit();
        else:
            QMessageBox.information(None, '提示', '恭喜你， 登录失败，用户名或密码错误！')

        cursor.close()
        conn.close()