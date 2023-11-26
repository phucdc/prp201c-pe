import sqlite3
import re

try:
     con = sqlite3.connect('EMPLIST.sqlite')
     con.executescript(
          '''
          drop table if exists DEPT;
          drop table if exists EMP;
          create table DEPT(
               DeptID text primary key,
               DName text not null   
          );
          
          create table EMP (
               ID text primary key,
               Name text not null,
               DeptID text not null,
               foreign key(DeptID) references DEPT(DeptID)
          );
          '''
     )
     
     with open('Dept.txt') as f:
          lines = f.readlines()
          for line in lines:
               if line.strip():
                    fields = re.split(r'\t+', line)
                    if fields[0] != 'ID':
                         did = fields[0]
                         dname = fields[1].strip()
                         con.execute('insert into DEPT(DeptID, DName) values(?,?)', (did, dname))
                         
          con.commit()
          
     with open('Data.txt') as f:
          lines = f.readlines()
          for line in lines:
               if line.strip():
                    fields = re.split(r'\t+', line)
                    if fields[0] != 'ID':
                         id = fields[0]
                         name = fields[1]
                         did = fields[2]
                         con.execute('insert into EMP(ID, Name, DeptID) values(?,?,?)', (id, name, did))   
          con.commit()
          
     table = con.execute("SELECT e.ID, e.Name, d.DName FROM EMP e INNER JOIN DEPT d ON e.DeptID = d.DeptID WHERE d.DeptID = 'CS' or d.DeptID = 'DA' ORDER by e.Name ASC;")
     print('Employee list:')
     print(f'{"ID":<10}{"Full Name":<20}{"Dept Name":<15}')
     for row in table:
          print(f'{row[0]:<10}{row[1]:<20}{row[2]:<15}')
     con.close()
except Exception as e:
     print(e)