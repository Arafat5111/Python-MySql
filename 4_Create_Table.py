import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("create table employeeInfo(Emp_ID int, Emp_Name varchar(55), Designation varchar(55), Salary decimal(15,2))")