"""
List the names of customers and their corresponding order number where a particular order from that customer
	    has a value greater than $25,000?

"""
import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select distinct(o.orderDate)) as 'Order Date',(select distinct (o.orderNumber)) as 'Order "
            "Number',(select distinct (c.customerNumber)) as 'Customer Number',(select distinct (c.customerName)) as "
            "'Customer Name', (select distinct(od.orderLineNumber)) as 'Oreder Line Number',(select distinct( "
            "od.productCode)) as 'Product Code',(select distinct (od.quantityOrdered)) as 'Quantitiy Ordered',"
            "(select distinct(od.priceEach)) as 'Price for Each' from orderdetails as od left join orders as o on "
            "o.orderNumber = od.orderNumber left join payments as p on p.customerNumber = o.customerNumber left join "
            "customers as c on c.customerNumber = p.customerNumber left join payments as py on py.customerNumber = "
            "c.customerNumber")

result = cur.fetchall()

for row in result:
    print(row)
