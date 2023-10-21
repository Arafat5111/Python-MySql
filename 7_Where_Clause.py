import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("select * from employeeinfo where Designation = 'Manager'")
showResult = mycursor.fetchone()

for row in showResult:
    print(row)