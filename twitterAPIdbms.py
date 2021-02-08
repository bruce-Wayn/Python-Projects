import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

tWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People(id INTEGER PRIMARY KEY, name TEXT UNIQUE, retrieved INTEGER)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Follows(from_id INTEGER, to_id INTEGER, UNIQUE(from_id, to_id))''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('enter a tw account or quit:')
    if (acct == 'quit'):
        break
    if (len(acct)<1):
        cur.execute('SELECT id, name FROM People WHERE retrieved = 0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',(acct,))
        try:
            id = cur.fetchone()[0]      #if the person is not in the table then try will fail and it will add it as a new value
        except:
            cur.execute('''INSERT OR IGNORE INTO People(name, retrieved) VALUES(?,0)''', (acct,))
            conn.commit()

            if (cur.rowcount !=1):
                print('error inserting the account', acct)
                continue
            id = cur.lastrowid



    url = twurl.augment(tWITTER_URL, {'screen_name': acct,'count':'100'})
    print('Retrieving account', acct)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except:
        print('unable to parse')
        print(data)
        break


    if 'users' not in js:
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('UPDATE People SET retrieved=1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js['users']:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrieved)
                        VALUES (?, 0)''', (friend, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, ' revisited=', countold)
    print('Remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()

#after adding your follows you can add follows of your friends and if they have a friend in common you get a 1 and also when you add the name of the 2nd one
#they also get a one
#that is we revisited someone and that is how we got a 1
#do it side by side sqllite to understand properly
