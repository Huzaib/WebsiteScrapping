import sqlite3
conn = sqlite3.connect('myquotes.db')
curr = conn.cursor()

curr.execute('''create table quotes_tb(
                question text
                )''')

curr.execute('''insert into quotes_tb values('python is awesome')''')
conn.commit()
conn.close()