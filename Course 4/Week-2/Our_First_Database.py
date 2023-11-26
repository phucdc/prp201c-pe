import sqlite3

conn = sqlite3.connect("OurFirstDatabase.sqlite")

# Drop the table if existed
conn.executescript('''
    DROP TABLE IF EXISTS Ages;

    CREATE TABLE Ages ( 
        name VARCHAR(128), 
        age INTEGER
    )
''')

# Insert into new table
conn.executescript('''
    INSERT INTO Ages (name, age) VALUES ('Riva', 32);
    INSERT INTO Ages (name, age) VALUES ('Eubha', 32);
    INSERT INTO Ages (name, age) VALUES ('Kirstyn', 40);
    INSERT INTO Ages (name, age) VALUES ('Bodhan', 29);
    INSERT INTO Ages (name, age) VALUES ('Samanthalee', 25);
''')

# They said they just want the first row, so i used LIMIT 1 :))
print(conn.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X LIMIT 1").fetchall())