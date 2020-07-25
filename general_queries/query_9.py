"""

List products sold by order date.


"""
import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select o.orderDate,p.productName,py.amount from customers as c left join payments as py on "
            "py.customerNumber = c.customerNumber join orders as o on o.customerNumber = py.customerNumber left join "
            "orderdetails as od on od.orderNumber = o.orderNumber left join products as p on od.productCode =  "
            "p.productCode group by p.productName ,o.orderDate  ,py.amount order by o.orderDate")

result = cur.fetchall()

for row in result:
    print(row)
