import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("update employeeinfo set Salary=80000 where Emp_ID = 102")
con.commit()
