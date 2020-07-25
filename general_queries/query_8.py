"""
Report the number of orders 'On Hold' for each customer.

"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select distinct (c.customerName)) as 'Customer Name',(select distinct count(o.orderNumber)) as "
            "'Order Number',(select distinct(o.status)) as 'Status' from customers as c left join orders as  o on "
            "o.customerNumber = c.customerNumber left join orderdetails as od on od.orderNumber = o.orderNumber where "
            "status = 'On Hold' group by o.status ,o.orderNumber,c.customerName order by c.customerName")

result = cur.fetchall()

for row in result:
    print(row)
