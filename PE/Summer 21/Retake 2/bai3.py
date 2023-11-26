import sqlite3
import re

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'MovieList.txt'
            inFile = open(filename, 'r') # cursor
            lines = inFile.readlines() # [dong1, dong2, ..., dong n]
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')

lines = getLines()
conn = sqlite3.connect('Movie.sqlite')
conn.executescript(
    '''
    drop table if exists MovieList;
    create table MovieList (
        movieID not null,
        length integer not null,
        Des not null
    );
    '''
)

for line in lines:
    fields = re.split(r'\s+', line)
    if fields[0] == 'MovieID':
        continue
    des = ''
    if fields[0].startswith('Act'):
        des = 'Action Movie'
    else:
        des = 'Scientific Movie'
    conn.execute('insert into MovieList values (?, ?, ?);', (fields[0], int(fields[1]), des))

conn.commit()
tables = conn.execute('select * from MovieList order by length desc;')
print('Movie list:')
print('%10s %10s %10s' % ('MovieID', 'Length', 'Description'))
for row in tables:
    print('%10s %10d %10s' % (row[0], row[1], row[2]))