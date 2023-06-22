import sqlite3
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()
conn.commit()

#cursor.execute("DELETE from tblfilms WHERE filmID == 1")

conn.commit()

def delete():
    #use the primary key to updated a record
    idField = input('Enter ID of the film to be deleted: ')

    'delete from songs where songID = 1/2/3'
    cursor.execute(f'delete from tblfilms where filmID = {idField}')
    conn.commit()
    print(delete)
    


if __name__ =='__main__':
    delete()
