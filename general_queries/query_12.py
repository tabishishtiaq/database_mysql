"""
Are there any products that appear on all orders ?


"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select od.orderNumber, od.productCode,p.productLine ,p.productName from  orderdetails as od left join "
            "products as p on p.productCode = od.productCode where od.productCode = p.productCode")

result = cur.fetchall()

for row in result:
    print(row)
