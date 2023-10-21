import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111", database="pythondb")

mycursor = con.cursor()
mycursor.execute("insert into employeeinfo(Emp_ID, Emp_Name, Designation, Salary) values(101, 'Alvee', 'Programmer', 70000)")

# insertdata = "insert into employeeinfo(Emp_ID, Emp_Name, Designation, Salary) values (%s,%s,%s,%s)" # Using Tuple

# records = [
#     (102, "Arafat", "Manager", 90000),
#     (103, "Jahid", "Programmer", 70000),
#     (104, "Imran", "Programmer", 70000),
# ]

# mycursor.executemany(insertdata, records)
con.commit()