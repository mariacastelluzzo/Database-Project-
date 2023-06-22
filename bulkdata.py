import sqlite3
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()
conn.commit()

def bulkData():
    #load SQL file
    with open("filmvalues.sql") as filmsDataFile:
        #create a variable sqlInsertData and pass the data read from the songs>DataFile using the red method
        sqlInsertData = filmsDataFile.read()
        #insert data stored in the variable sqlInsertData
        cursor.executescript(sqlInsertData)
        #PER AGGIUNGERE UN VALORE cursor.execute(INSERT.......)
      
        #call the read function frm the readsons file to read data from teh table songs
        #readfilms()

if __name__=='__main__':
    bulkData()
