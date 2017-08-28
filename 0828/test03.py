'''
Created on 2017年8月28日

@author: Lin Yu
'''
import cx_Oracle

con = cx_Oracle.connect( "username", "password","databaseName")
cursor = con.cursor()
cursor.execute("select * from emp")
data = cursor.fetchone()
print (data)
cursor.close()
con.close()