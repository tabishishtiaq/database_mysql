"""
List the amount paid by each customer.
"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select distinct (c.customerName)) as 'Customer Name', (select distinct sum(p.amount)) as 'Total "
            "Payment By Each Customer' from customers as c right join payments as p ON p.customerNumber = "
            "c.customerNumber group by c.customerName order by c.customerName")

result = cur.fetchall()

for row in result:
    print(row)
