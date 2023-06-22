import sqlite3

conn = sqlite3.connect('filmflix.db')
#create cursor
cursor = conn.cursor()

#create a table
cursor.execute("""CREATE TABLE tblfilms (
    filmID INTEGER,
    title TEXT,
    yearReleased INTEGER,
    rating TEXT,
    duration INTEGER,
    genre TEXT
)""")

#commit command
conn.commit()

#close connection
conn.close()
 