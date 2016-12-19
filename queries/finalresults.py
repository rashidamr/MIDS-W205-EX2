
import psycopg2

import sys

if len(sys.argv) > 1:
        x = sys.argv[1]
else:
     	x = None

conn = psycopg2.connect(database="Tcount", user="w205", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("SELECT * FROM tweetwordcount ORDER BY word ASC;")
rows = cur.fetchall()

if x == None:

	for row in rows:
                print "word = ", row[0], "    ",  "count = ", row[1]

        print "Operation done successfully";

else:

     	for i in range (0, len(rows)):
                if rows[i][0]==x:
                        print "Total number of occurences of ",'"',rows[i][0],'"' , "is" ,rows[i][1]
        print "Operation done successfully";


conn.close()

