import sqlite3
con=sqlite3.connect('database.db')
cur=con.cursor()
cursor=cur.execute("SELECT * FROM my_table")
for q in cursor:
    print(q[0],"\t",q[1],"\t",q[2],"\t",q[3],"\t")
con.close()