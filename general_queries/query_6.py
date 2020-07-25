"""
Who are the employees in Boston?

"""
import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()

cur.execute("select concat(emp.firstName,' ', emp.lastName) as 'Employee Name',off.city from employees as emp left "
            "join offices  as off on off.officeCode = emp.officeCode where city = 'boston'")

result = cur.fetchall()

for row in result:
    print(row)
