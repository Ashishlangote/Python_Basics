# def counter():
#     num = 0
#
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#
#     return incrementer
#
#
# c = counter()
# print(c())  # = 1
# print(c())  # = 2
# print(c())  # = 3

# import sqlite3
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
# # Create table
# c.execute('''CREATE TABLE stocks
#  (date text, trans text, symbol text, qty real, price real)''')
# # Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# # Save (commit) the changes
# conn.commit()
# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
a = c.fetchall()  # which is similar to list(cursor) method used previously
for row in a:
    print(row)

name_lengths = map(len, ["Mary", "Isla", "Sam"])
print(list(name_lengths))
