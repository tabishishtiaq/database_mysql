"""
Report the account representative for each customer

"""





import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()


cur.execute("select(select distinct (c.customerName)) as 'Customer Name',(select distinct (c.salesRepEmployeeNumber)) as 'Account Representative',(select distinct (e.firstName)) as 'Employee First Name',(select distinct (e.lastName)) as 'Employee Last NAme' from customers as c left join employees as e on e.employeeNumber = c.salesRepEmployeeNumber where salesRepEmployeeNumber is not null order by customerName")

result = cur.fetchall()

for row in result:
    print(row)