import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("select * from employeeinfo")
# mycursor.execute("select max(Salary) from employeeinfo")
showResult = mycursor.fetchall()

for row in showResult:
    print(row)
