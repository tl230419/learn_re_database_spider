'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='day26', charset='utf8')
cursor = conn.cursor()

sql = """update user set money=10000 where id = 1;"""
row_count = cursor.execute(sql)
print("SQL语句执行影响的行数%d" % row_count)

conn.rollback()

cursor.close()
conn.close()