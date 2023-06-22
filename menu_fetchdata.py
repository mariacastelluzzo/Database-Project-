import sqlite3
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()
# fetches all selected items

def year():
    yearField = input("Enter the year when the film was released: ")
    cursor.execute(F"SELECT * FROM tblfilms WHERE yearReleased = '{yearField}' ")    
    items = cursor.fetchall() 
    for item in items:
        print(item)

    if yearField not in items: 
        print(f"Sorry {yearField} doesn't match with our records")
    return yearField
    
    

def rating():
    ratingField = input("Enter the rating of the film to search for: ")
    cursor.execute(F"SELECT * FROM tblfilms WHERE rating = '{ratingField}' ")
    items = cursor.fetchall() 
    for item in items:
        print(item)

    if ratingField not in items: 
        print(f"Sorry {ratingField} doesn't match with our records")
    return ratingField

def genre():
    genreField = input("Enter the name of the film to search for: ")
    cursor.execute(F"SELECT * FROM film WHERE genre = '{genreField}' ")
    items = cursor.fetchall() 
    for item in items:
        print(item)
    
    if genreField not in items: 
        print(f"Sorry {genreField} doesn't match with our records")
    return genreField

def readOrder():
    cursor.execute("SELECT * FROM tblfilms ORDER BY filmID ASC")
    items = cursor.fetchall() 
    for item in items:
        print(item)




if __name__ == "__main__":
    #readOrder()
    #genre()
    #rating()
    year()






















