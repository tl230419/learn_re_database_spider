'''
*****************
Date: 2020-05-06
Author: Allen
*****************
'''

from pymysql import connect

def main():
    find_name = input("请输入物品名称：")

    conn = connect(host='localhost', port=3306, user='root', password='123456', database='day26', charset='utf8')
    cs1 = conn.cursor()

    param = [find_name]
    count = cs1.execute('select * from user where name = %s', param)
    print(count)
    result = cs1.fetchall()
    print(result)
    cs1.close()
    conn.close()

if __name__ == '__main__':
    main()