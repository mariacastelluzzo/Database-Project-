import sqlite3
import readfilms
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()


def update():
    #use the primary key to update a record
    idField = int(input('Enter ID of film to be update: '))
        
    newTitle = input('Enter new title: ')
    
    newYearReleased = int(input('Enter new year: '))
   
    newRating = input('Enter new rating: ')
    
    newDuration = int(input('Enter new duration: '))
   
    newGenre = input('Enter new genre:  ')
    

    'update films set Title/Artist/Genre = TitleValue/yearReleasedValue/ratingValue/durationValue/genreValue where filmID = 1/2/3'
    #cursor.execute(f'UPDATE tblfilms SET title = {newTitle}, yearReleased = {newYearReleased}, rating = {newRating}, duration = {newDuration}, genre = {newGenre}   WHERE filmID = {idField}')
    cursor.execute('UPDATE tblfilms SET title = ?, yearReleased = ?, rating = ?, duration = ?, genre = ?  WHERE filmID = ?',(newTitle, newYearReleased, newRating, newDuration, newGenre, idField))
    conn.commit()#make the change permanent
    print(f'Record {idField} updated in the film table')





if __name__ =='__main__':
    update()