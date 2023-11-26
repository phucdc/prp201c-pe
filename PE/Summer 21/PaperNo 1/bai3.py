import sqlite3
import re

try:
    cur = sqlite3.connect('DNSList.sqlite')
    cur.executescript(
        '''
            drop table if exists DNS;
            create table DNS (
                IP not null primary key unique,
                Reliability integer,
                Description not null
            );
        '''
    )

    f = open('DNSList.txt', 'r')
    lines = f.readlines()

    for line in lines:
        if 'IP' in line:
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)[0]
        if 'Reli' in line:
            reli = int(re.search(r'[0-9]+', line)[0])
            if reli >= 50:
                des = 'Normal'
            else:
                des = 'Low'
            cur.execute('insert into DNS values (?, ?, ?)', (ip, reli, des))
    cur.commit()

    table = cur.execute('select * from DNS order by Reliability desc')
    print('DNS server list:')
    print('IP'.ljust(20, ' ') + 'Reliability'.ljust(15, ' ') + 'Description'.ljust(11, ' '))
    for row in table:
        print(row[0].ljust(20, ' ') + str(row[1]).ljust(15, ' ') + row[2].ljust(11, ' '))

    f.close()
    cur.close()

except Exception as e:
    print(e)
