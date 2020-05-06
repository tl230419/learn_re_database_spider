'''
*****************
Date: 2020-05-05
Author: Allen
*****************
'''

import pymysql
import random

conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456")
cursor = conn.cursor()
cursor.execute("create database if not exists test_index")
cursor.execute("use test_index")
cursor.execute("create table if not exists emp(id int primary key, name varchar(10), age int, sal double)")

print("start insert!")
for i in range(5000000):
    name = "n" + str(i)
    age = random.randrange(1, 100)
    sal = random.randrange(1000, 5000)
    cursor.execute("insert into emp values(%s,%s,%s,%s)", args=[i,name,age,sal])
    print("insert %d" % (i + 1))

conn.commit()
conn.close()
print("finish!")