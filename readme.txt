Instructions:

The app runs on a fresh instance of: UCB MIDS W205 EX2-FULL

Steps to run the App:

1) Connect to the machine via ssh
2) su - w205
3) git clone https://github.com/rashidamr/MIDS-W205-EX2.git
4) cd MIDS-W205-EX2

5) ./pips.sh   (installs tweepy & psycopg2)
6) ./postgres.sh  (starts & initiates postgres database)
7) ./run.sh


Steps to query data:

 python /home/w205/MIDS-W205-EX2/queries/finalresults.py
 python /home/w205/MIDS-W205-EX2/queries/finalresults.py word
 python /home/w205/MIDS-W205-EX2/queries/histogram.py 100 200
 python /home/w205/MIDS-W205-EX2/queries/graph.py
