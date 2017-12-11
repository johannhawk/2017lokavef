import sqlite3
conn = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
conn.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, desc TEXT, datetime TEXT)")
conn.execute(
    "INSERT INTO todo (title,desc,datetime) VALUES ('Read A-byte-of-python to get a good introduction into Python','texti','timi')")
conn.execute("INSERT INTO todo (title,desc,datetime) VALUES ('Klara verkefni','texti','timi')")
conn.commit()