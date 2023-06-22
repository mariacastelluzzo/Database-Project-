import sqlite3
import add_a_new_record
import amend_a_record
import delete_a_record
import readfilms
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()
conn.commit()

def menu():

    options = 1 #true

    menuOption =    {1: "Add a new record",
                     2: "Delete a record", 
                     3: "Amend a record",
                     4: "Print all records",
                     5: "Exit"}
    
    options = int(input("Enter an option from the main menu choices above: "))

            #selection 
    if options not in menuOption: 
            print(f"{options} is not a valid choice in the menu")
    return options


mainProgram = True # assign  mainProgram a true boolean variable
while mainProgram: 
    mainMenu = menu() # assign the menu function to the variable mainMenu
    if mainMenu == 1: 
        # go into the file  and call/invoke the respective function 
        add_a_new_record.insertfilms()
    elif mainMenu == 2:
        delete_a_record.delete()
    elif mainMenu == 3:
        amend_a_record.update()
    elif mainMenu == 4:
        readfilms.readfilms()
    elif mainMenu == 5:
        print("Exit")
        break
    else:
        print("Your choice was invalid, try again")

    






    

