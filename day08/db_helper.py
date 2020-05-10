import pymysql
import re

def create_db():
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", charset="utf8")
    cursor = conn.cursor()
    cursor.execute("create database if not exists itmovie")
    cursor.execute("use itmovie")
    cursor.execute("create table if not exists t_movie(id int primary key auto_increment, img_url varchar(255), title varchar(100), download_url varchar(100))")
    cursor.close()
    print("create db...")

def save(detail):
    conn = pymysql.connect(host="localhost", port=3306, database="itmovie", user="root", password="123456")
    cursor = conn.cursor()
    ret = cursor.execute("insert into t_movie values(null, %s, %s, %s)", detail)
    print("保存结果：", ret)
    cursor.close()
    conn.commit()

def fetch_movies():
    conn = pymysql.connect(host="localhost", port=3306, database="itmovie", user="root", password="123456")
    cursor = conn.cursor()
    cursor.execute("select * from t_movie")
    result_list = cursor.fetchall()
    return result_list