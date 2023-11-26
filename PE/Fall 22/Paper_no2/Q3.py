import sqlite3
import re

try:
     con = sqlite3.connect('PRODUCT.sqlite')
     con.executescript(
          '''
          drop table if exists CATEGORY;
          drop table if exists PRODUCT;
          create table CATEGORY(
               CatID text primary key,
               CatName text not null   
          );
          
          create table PRODUCT (
               PID text primary key,
               PName text not null,
               CatID text not null,
               foreign key(CatID) references CATEGORY(CatID)
          );
          '''
     )
     
     with open('Category.txt') as f:
          lines = f.readlines()
          for line in lines:
               if line.strip():
                    fields = re.split(r'\s+', line)
                    if fields[0] != 'ID':
                         catid = fields[0]
                         catname = fields[1]
                         con.execute('insert into CATEGORY(CatID, CatName) values(?,?)', (catid, catname))
                         
          con.commit()
          
     with open('Product.txt') as f:
          lines = f.readlines()
          for line in lines:
               if line.strip():
                    fields = re.split(r'\t+', line)
                    if fields[0] != 'ID':
                         pid = fields[0]
                         pname = fields[1]
                         catid = fields[2]
                         con.execute('insert into PRODUCT(PID, PName, CatID) values(?,?,?)', (pid, pname, catid))   
          con.commit()
          
     table = con.execute("SELECT p.PID, p.PName, c.CatName FROM PRODUCT p INNER JOIN CATEGORY c ON  p.CatID = c.CatID WHERE p.CatID = 'TV' OR p.CatID = 'PH' ORDER BY p.PName DESC;")
     print('PRODUCT LIST')
     print(f'{"ID":<10}{"Product Name":<20}{"Category":<15}')
     for row in table:
          print(f'{row[0]:<10}{row[1]:<20}{row[2]:<15}')
     con.close()
except Exception as e:
     print(e)