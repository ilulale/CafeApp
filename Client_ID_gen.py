import sqlite3
conn=sqlite3.connect('lmao.db')
c=conn.cursor()

def client_def():
    #will include account details too
    c.execute('CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY, name TEXT)')
    c.execute('INSERT INTO names(name) VALUES(?)', ('Test',))
    c.execute('INSERT INTO names(name) VALUES(?)', ('Test1',))
    c.execute('INSERT INTO names(name) VALUES(?)', ('Test2',))
    conn.commit()
    c.execute('SELECT * FROM names')
    rows = c.fetchall()
    for row in rows:    
        pass
    return(row)
    #returns ID of last entry
   

x=client_def()
print(x)
