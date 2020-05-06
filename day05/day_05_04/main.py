'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

from pymysql import connect
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction
from register_widget import RegisterWidget
from login_widget import LoginWidget
from index_widget import IndexWidget
import sys

class StuSystem:
    def __init__(self):
        app = QApplication(sys.argv)

        self.main_window = QMainWindow()
        self.main_window.setFixedSize(800,400)

        menu_bar = self.main_window.menuBar()
        operation = menu_bar.addMenu("操作")

        login_action = QAction("登录")
        operation.addAction(login_action)
        login_action.triggered.connect(self.show_login)

        register_action = QAction("注册")
        operation.addAction(register_action)
        register_action.triggered.connect(self.show_register)

        self.show_index()

        self.main_window.show()
        sys.exit(app.exec())

    def show_index(self):
        print("显示主要功能页")
        index_widget = IndexWidget()
        self.main_window.setCentralWidget(index_widget)

    def show_login(self):
        print("显示登录页面")
        login_widget = LoginWidget()
        login_widget.login_success.connect(self.show_index)
        self.main_window.setCentralWidget(login_widget)

    def show_register(self):
        print("显示注册页面")
        register_widget = RegisterWidget()
        register_widget.register_success.connect(self.show_login)
        self.main_window.setCentralWidget(register_widget)

    def create_db(self):
        conn = connect(host="localhost", port=3306, user="admin", password="123456")
        cursor = conn.cursor()

        sql = "create database if not exists itheima"
        cursor.execute(sql)
        cursor.execute("use itheima")
        sql = """create table if not exists user(
        id int primary key auto_increment,
        username varchar(20),
        password varchar(50),
        nickname varchar(20)
        );"""

        cursor.execute(sql)

        sql = """create table if not exists student(
                sid int primary key auto_increment,
                name varchar(20),
                age int,
                gender varchar(2)
                );"""
        cursor.execute(sql)

        cursor.close()
        conn.close()

if __name__ == '__main__':
    StuSystem()

