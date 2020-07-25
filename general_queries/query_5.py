"""
How many orders have been placed by Herkku Gifts?

"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select c.customerName,count(o.orderNumber) as 'Orders' from customers  as c left join orders as o on "
            "o.customerNumber = c.customerNumber left join orderdetails as od on od.orderNumber = o.orderNumber where "
            "c.customerName = 'herkku gifts'")

result = cur.fetchall()

for row in result:
    print(row)
