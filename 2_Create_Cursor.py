import mysql.connector
con = mysql.connector.connect(host="localhost", user="arafat", passwd="5111")

mycursor = con.cursor()
mycursor.execute("create database pythonara")