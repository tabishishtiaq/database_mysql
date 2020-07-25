"""
What are the names of executives with VP or Manager in their title? Use the CONCAT function to combine the
	    employee's first name and last name into a single field for reporting.
"""

import pymysql

mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()


cur.execute("SELECT employeeNumber,extension,email,officeCode,reportsTo,jobTitle,concat(firstName,lastName) as 'FULL NAME' FROM employees where jobTitle like '%VP%' or '%Manager%' ")

result = cur.fetchall()

for row in result:
    print(row)