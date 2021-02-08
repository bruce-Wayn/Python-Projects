#DBMS emails extraction into sql file and keeping count
#mbox.txt is a txt file where data is already extracted
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts (email TEXT, count INTEGER)''')

fh = open('mbox.txt')

for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))       #the ? is for preventing sql injection, and (email,) is a tuple
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email,count)
                VALUES (?,1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',(email,))     #email tuple relaces ?
    conn.commit()

#now we are going to read the database
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'     #limit 10 does top 10, sorting with desc
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

#remaining : roster, Tracks, Twfriends, Twspider
