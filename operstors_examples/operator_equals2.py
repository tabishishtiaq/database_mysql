"""

"""

"""
Report total payments for Atelier graphique.
"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select (select distinct( c.customerNumber)) as 'Customer Number',(select distinct( c.customerName)) as 'Customer Name',(select distinct sum(p.amount)) as 'Total Payment' from customers as c left join payments as p on p.customerNumber = c.customerNumber where customerName = 'Atelier graphique' group by c.customerName,c.customerNumber")

result = cur.fetchall()

for row in result:
    print(row)