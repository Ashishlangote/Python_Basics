import pymysql

conn = pymysql.connect(host='localhost', user='root', password="ashish", db='login')

cur = conn.cursor()
cur.execute("select * from users")
# output = cur.fetchall()

for i in cur:
	print(i)
# print(output)
conn.close()
