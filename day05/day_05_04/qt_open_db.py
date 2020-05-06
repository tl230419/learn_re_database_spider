'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

import QSqlDatabase

db = QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setPort(3306)
db.setUsername("admin")
db.setPassword("123456")
db.setDatabaseName("itheima")

db.open()

query = QSqlQuery(db)
query.exec("""
            create table if not exists student(
            sid int primary key,
            name varchar(20),
            age int,
            sex varchar(2)
            );""")

def test_query(db):
    query = QSqlQuery(db)
    ret = query.exec("select * from student;")
    print(ret)
    while query.next():
        print(query.value(0))
        print(query.value(1))
        print(query.value(2))
        print(query.value(3))
        print("=======================")

def test_insert(db):
    query = QSqlQuery(db)
    ret = query.exec("insert into student values(%d, '%s', %d, '%s')" % (2001,"老王",36,"男"))
    print(query.lastError().text())
    print(ret)

def test_update(db):
    query = QSqlQuery(db)
    ret = query.exec("update student set name='%s' where name='%s'" % ("小王","老王"))
    print(query.lastError().text())
    print(ret)

def test_delete(db):
    query = QSqlQuery(db)
    ret = query.exec("delete from student where sid=%d" % 2001)
    print(query.lastError().text())
    print(ret)
