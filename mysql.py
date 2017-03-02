#
import pymysql
conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234567',
        db='test')
cur=conn.cursor()
ret=cur.execute('create table ab(a varchar(10),b int)')
print(ret)
cur.close()
conn.close()
print(conn)
