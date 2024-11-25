
import sqlite3

conn=sqlite3.connect('test.db')

print('Datubāze ir atvērta!')

cursor=conn.execute("SELECT * from COMPANY")
for ieraksts in cursor:
    print ("ID=", ieraksts[0])
    print ("NAME=", ieraksts[1])
    print ("AGE=", ieraksts[2])
    print ("ADRESS=", ieraksts[3])
    print ("SALARY=", ieraksts[4], "\n")
print("Dati ir veiksmīgi nolasīti!")
 
'''conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADRESS, SALARY)\
             VALUES(1, 'Andrejs', 18, 'Rezekne', 20000.00)");

conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADRESS, SALARY) \
    VALUES(2, 'Dima', 20, 'Riga', 13000.00)");

conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADRESS, SALARY) \
    VALUES(3, 'Aleksa', 21, 'Riga', 26000.00)");

conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, ADRESS, SALARY) \
    VALUES(4, 'Vika', 34, 'Ventspils', 97000.00)");

conn.commit()
print("Ieraksti ir izveidoti")'''

"""
conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY  NOT NULL,
             NAME      TEXT       NOT NULL,
             AGE       INT        NOT NULL,
             ADRESS    CHAR(50),
             SALARY    REAL);''')
print('Tabula ir izveidota!')
"""

conn.close()
