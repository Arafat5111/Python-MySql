import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111")
print(con)
if(con):
    print("Connection Successfull")
else:
    print("Connection Unsuccessfull")
    