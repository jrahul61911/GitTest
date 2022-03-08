import mysql.connector

from utilities.configurations import *
from utilities import *

conn = getConnection()
# conn = mysql.connector.connect(host='localhost',database='employees',user='root',password='6191')
# print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from departments')
row = cursor.fetchone()
row_fetachall = cursor.fetchall()
print(row)
print(row_fetachall)

# query = "update departments set dept_name= %s where dept_no = %s"
# data = ("Engineering", "d005")
# cursor.execute(query, data)
# conn.commit()

# conn.close()
