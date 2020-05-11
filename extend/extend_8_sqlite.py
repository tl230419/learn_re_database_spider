'''
*****************
Date: 2020-05-11
Author: Allen
*****************
'''

import sqlite3

# create db
conn = sqlite3.connect("test.db")

import os
#os.remove("test.db")

cursor = conn.cursor()
# create table
# sql = """create table stu(
#             id integer primary key autoincrement,
#             name varchar(20),
#             age integer,
#             salary double
#            )
#        """
# cursor.execute(sql)
#
# cursor.execute("drop table stu")

# insert
sql = "insert into stu(name,age,salary) values(?,?,?)"
cursor.execute(sql,["张三",18,20.12])
conn.commit()

# update
sql = "update stu set name=? where id=?";
cursor.execute(sql,["老三",1])
conn.commit()

# delete
sql = "delete from stu where id = ?";
cursor.execute(sql,[1])
conn.commit()