import pymysql


mydb = pymysql.Connect(host="localhost", user="root", password="mysql1pwd", database="classicmodels")

host = mydb.get_host_info()
cur = mydb.cursor()


"""
    What is the average percentage markup of the MSRP on buyPrice?
	    

"""

cur.execute("select *, AVG(MSRP/buyPrice) as 'Avg Markup' from products group by productCode")

result = cur.fetchall()

for row in result:
    print(row)