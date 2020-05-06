'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlTableModel,QSqlDatabase
from PyQt5.QtCore import Qt

class IndexWidget(QWidget):
    def __init__(self):
        super(IndexWidget, self).__init__()

        hbox = QHBoxLayout(self)
        group_box = QGroupBox("数据库操作")
        hbox.addWidget(group_box)
        vbox = QVBoxLayout()
        group_box.setLayout(vbox)

        query_btn = QPushButton("查看数据")
        query_btn.clicked.connect(self.query_db)
        vbox.addWidget(query_btn)

        add_btn = QPushButton("增加一行")
        add_btn.clicked.connect(self.add)
        vbox.addWidget(add_btn)

        delete_btn = QPushButton("删除一行")
        delete_btn.clicked.connect(self.delete)
        vbox.addWidget(delete_btn)

        exit_btn = QPushButton("退出")
        exit_btn.clicked.connect(QApplication.exit)
        vbox.addWidget(exit_btn)

        self.table_view = QTableView()
        hbox.addWidget(self.table_view)

        db = QSqlDatabase.addDatabase("QMYSQL")
        db.setHostName("localhost")
        db.setPort(3306)
        db.setUserName("admin")
        db.setPassword("123456")
        db.setDatabaseName("itheima")

        db.open()

        self.table_model = QSqlTableModel(db=db)
        self.table_model.setTable("student")
        self.table_model.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.table_model.setHeaderData(0, Qt.Horizontal, "学号")
        self.table_model.setHeaderData(1, Qt.Horizontal, "姓名")
        self.table_model.setHeaderData(2, Qt.Horizontal, "年龄")
        self.table_model.setHeaderData(3, Qt.Horizontal, "性别")

        self.table_view.setModel(self.table_model)

    def query_db(self):
        print(self.table_model.lastError().text())
        self.table_model.select()

    def add(self):
        self.table_model.insertRow(self.table_model.rowCount())

    def delete(self):
        index = self.table_view.currentIndex().row()
        self.table_model.removeRow(index)
        self.table_model.select()