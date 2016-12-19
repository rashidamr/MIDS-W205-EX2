
import psycopg2

conn = psycopg2.connect(database="Tcount", user="w205", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor.

cur = conn.cursor()
cur.execute('''DROP TABLE IF EXISTS Tweetwordcount;''')
conn.commit()

cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()

conn.close()