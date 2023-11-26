import requests
import sqlite3
import re

conn = sqlite3.connect('org.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Counts;
    CREATE TABLE Counts (org TEXT, count INTEGER)
''')

url = "https://www.py4e.com/code3/mbox.txt?PHPSESSID=565f7a38ac8592bb5395ff4ed0f6f188"
res = requests.get(url)
lines = res.text.split('\n')

for line in lines:
    if not line.startswith('From: '): continue
    fields = line.split()
    pos = fields[1].find('@')
    org = fields[1][pos+1:len(fields[1])]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()