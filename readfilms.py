from connect import *

def readfilms(): #read the data 
    cursor.execute('select * from tblfilms') 
    films = cursor.fetchall() # another method that fetched the data or selected records
    

    for aFilm in films:
        print(aFilm)
if __name__ =='__main__':
    readfilms()#call/invoke the function