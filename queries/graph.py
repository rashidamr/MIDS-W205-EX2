
import psycopg2


conn = psycopg2.connect(database="Tcount", user="w205", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute("SELECT * FROM tweetwordcount ORDER BY count DESC LIMIT 102;")
rows = cur.fetchall()

m = ("there", "am", "the", "to", "a", "if", "I", "you", "is", "and",\
 "for", "in", "this", "my", "so", "me", "on", "with", "The", "are", \
 "have","at","of","that","in","i","just","&amp","they","be","I'm", \
 "it", "your", "-", "when", "will", "can", "but", "as", "who", "from", \
 "we", "what", "all", "You", "get", "by", "not", "don't", "THE", "out", \
 "was", "one", "A", "their", "them", "how", "up", "SO", "about", "This", "OF", \
 "do", "has", "u", "our", "THEY", "go", "his", "he", "Me", "us", "would", "him", \
 "IS", "1", "We", "been", "had", "want", "need", "or", "got", "When", "know", \
 "day", "why", "think", "going", "an", "New", "What", "If")



for i in range (0, len(rows)):
	if rows[i][0] not in m:
		print "word = ", rows[i][0], "    ",  "count = ", rows[i][1]

print "Operation done successfully";


conn.close()

