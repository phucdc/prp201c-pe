import sqlite3
import re

try:
    cur = sqlite3.connect('Trace.sqlite')
    cur.executescript(
        '''
            drop table if exists providers;
            create table providers(
                pname not null primary key,
                pcount int not null,
                pwarning not null
            );   
        '''
    )

    f = open('Trace.txt', 'r')
    lines = f.readlines()

    traces = {}

    for line in lines:
        if 'Name' in line:
            provider = re.search(r'(?<=\s)(\w+?)(?=\-)', line)[0]
            if provider not in traces:
                traces[provider] = 1
            else:
                traces[provider] += 1
    
    for provider in traces:
        if traces[provider] > 1:
            pwarning = 'High risk'
        else:
            pwarning = 'Normal'
        cur.execute('insert into providers values (?, ?, ?)', (provider, traces[provider], pwarning))
    cur.commit()

    table = cur.execute('select * from providers order by pcount desc')
    print('Troubleshot wired LAN related issues:')
    print('Provider'.ljust(15, ' ') + 'Count'.ljust(10, ' ') + 'Warning'.ljust(11, ' '))
    for row in table:
        print(row[0].ljust(15, ' ') + str(row[1]).ljust(10, ' ') + row[2].ljust(11, ' '))

    f.close()
    cur.close()

except Exception as e:
    print(e)
