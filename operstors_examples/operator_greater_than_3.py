"""
Report those payments greater than $100,000. Sort the report so the customer who made the highest payment appears
	    first.
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select distinct (c.customerName)) as 'Customer Name', (select distinct sum(p.amount)) as 'Total "
            "Payment By Each Customer' from customers as c right join payments as p ON p.customerNumber = "
            "c.customerNumber where p.amount > 100000 group by c.customerNumber,p.amount order by p.amount desc")

result = cur.fetchall()

for row in result:
    print(row)
