"""
Report the name and city of customers who don't have sales representatives?

"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()


cur.execute(" SELECT * FROM customers where salesRepEmployeeNumber is null")

result = cur.fetchall()

for row in result:
    print(row)