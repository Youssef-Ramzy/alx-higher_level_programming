#!/usr/bin/python3
""" This script is to list all the states from hbtn_0e_0_usa database """
import MySQLdb

mydb =MySQLdb.connect(
	host="localhost",
	port=3306,
	user="root",
	passwd="root",
	database="hbtn_0e_0_usa"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT id, name FROM states ORDER BY id;")
for row in mycursor.fetchall():
    print(row)
