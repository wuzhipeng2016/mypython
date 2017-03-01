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

print(connection)

try:
    with connection.cursor() as cursor:
        sql='select a,b from abc'
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
    connection.commit()
finally:
    connection.close()
