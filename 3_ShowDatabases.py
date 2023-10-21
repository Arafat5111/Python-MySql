import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111")

mycursor = con.cursor()
mycursor.execute("show databases")
for db in mycursor:
    print(db)