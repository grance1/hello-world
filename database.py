#!/usr/bin/python2.7
import MySQLdb

conn = MySQLdb.connect(host = "127.0.0.1", user = "root", passwd ='123', db = "db_house_price")
cursor = conn.cursor()
cursor.execute('insert into Nanjing (Name,Price) values (%s, %s)', ['nj', 99])
print cursor.rowcount


conn.commit()
#cursor.close()
#cursor = conn.cursor()
cursor.execute('select * from Nanjing where Name = %s', ('nj',))
values = cursor.fetchall()
print values
cursor.close()

conn.close()
