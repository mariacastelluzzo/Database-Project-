import sqlite3
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()


def insertfilms():
    films = []

    filmID = input('Enter film ID: ')
    title = input('Enter film title: ')
    yearReleased = input('Enter film year of release: ')
    rating = input('Enter film rating: ')
    duration = input('Enter film duration: ')
    genre = input('Enter film genre: ')



    films.extend([filmID, title, yearReleased, rating, duration, genre])
    
    cursor.execute("INSERT INTO tblfilms(filmID, title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?, ?)", films)
    conn.commit()

    print(f'{title} inserted into table films')


    if __name__ =='__main__':
      insertfilms()



#cursor.execute("INSERT INTO tblfilms(filmID, Title, yearReleased, rating, duration, genre) VALUES (1, 'Citizen Kane', 1941, '8.3', 119, 'Drama')")

conn.commit()#commit the change pemanently



 


    

