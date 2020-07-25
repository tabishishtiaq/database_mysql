"""
Report the products that have not been sold.
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select productName ,quantityInStock from products order by productLine")

result = cur.fetchall()

for row in result:
    print(row)

