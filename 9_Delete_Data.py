import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("delete from employeeinfo where Emp_ID = 104")

con.commit()
print("Record Deleted")
