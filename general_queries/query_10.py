"""
List the order dates in descending order for orders for the 1940 Ford Pickup Truck.


"""


import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select o.orderDate,p.productName from orders as o left join orderdetails as od on od.orderNumber = "
            "o.orderNumber left join products as p on p.productCode = od.productCode where productName = '1940 Ford "
            "Pickup Truck' group by o.orderDate,p.productName order by o.orderDate desc")

result = cur.fetchall()

for row in result:
    print(row)
