
import psycopg2

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])



conn = psycopg2.connect(database="Tcount", user="w205", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("SELECT * FROM tweetwordcount ORDER BY word ASC;")
rows = cur.fetchall()


for i in range (0, len(rows)):
        if rows[i][1] >= x:
                if rows[i][1] <= y:
                        print "word = ", rows[i][0], "    ",  "count = ", rows[i][1]

print "Operation done successfully";


conn.close()


