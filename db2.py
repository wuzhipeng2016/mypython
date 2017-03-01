import datetime
import pymysql.cursors
 
config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'1234567',
          'db':'test',
          'cursorclass':pymysql.cursors.DictCursor,
          }
connection = pymysql.connect(**config)

connection = pymysql.connect(user='root',password='1234567',host='localhost',port=3306,db='test')

print(connection)

try:
    cur = connection.cursor()
    cur.execute("select * from abc")
    result = cur.fetchall()
    print(result)
    #for r in cur:
    #    print(r)
    cur.close()
finally:
    connection.close()
