"""

	--	List the value of 'On Hold' orders.

"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select distinct (od.orderNumber)) as 'Order Number',(select distinct(o.status)) as 'Status' , "
            "(od.quantityOrdered )* (od.priceEach) as 'On Hold Orders value' from orders as  o left join "
            "orderdetails as od on od.orderNumber = o.orderNumber where status = 'On Hold' group by o.status,"
            "od.orderNumber,od.quantityOrdered,od.priceEach order by o.status")

result = cur.fetchall()

for row in result:
    print(row)
