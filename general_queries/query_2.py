"""
Report the total payments by date

"""

import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select(select  distinct (p.paymentDate)) as 'Payment Date',(select distinct sum(p.amount)) as 'Amount' from payments as p group by  p.paymentDate,p.amount order by p.paymentDate,p.amount")

result = cur.fetchall()

for row in result:
    print(row)
