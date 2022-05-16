import sqlite3
con = sqlite3.connect("example.db")
curs = con.cursor()

# Create table
curs.execute(''' CREATE TABLE ETUDIANT (
                 No integer primary key,
                 Name varchar not null,
                 Age integer not null)''')

# Insert Data
curs.execute("INSERT INTO ETUDIANT values (1,'AYMEN', 22)")
curs.execute("INSERT INTO ETUDIANT values (2,'MAIZIZ', 22)")
curs.execute("INSERT INTO ETUDIANT values (3,'ALAA', 24)")

# Query data
"""
for row in curs.execute("SELECT * FROM ETUDIANT"):
    print(row)
"""
"""
curs.execute("SELECT * FROM ETUDIANT")
print(curs.fetchmany(2))
"""
curs.execute(" SELECT * FROM ETUDIANT WHERE age=:age", {'age': 22})
print(curs.fetchall())
#  Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed, or they will be lost.
con.close()

