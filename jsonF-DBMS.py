#the data is already stored in a file extracted as json
import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#doing some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS COURSE;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) 
''')

str_data = open('roster_data_sample.json').read()
json_data = json.loads(str_data)

for inputdata in json_data:
    name = inputdata[0]
    title = inputdata[1]
    role = inputdata[2]
    print((name,title))
    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES(?)''',(name,))

    cur.execute('SELECT id FROM User WHERE name = (?)',(name,))
    User_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?',(title,))
    Course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?, ?, ?)''',(User_id, Course_id, role))

    conn.commit()
