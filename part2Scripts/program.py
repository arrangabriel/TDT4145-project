import sqlite3
from datetime import datetime

con = sqlite3.connect("coffeeDB.db")
cursor = con.cursor()
currentUser = None


def login():
    email = input("Email: ")
    password = input("Password: ")
    
    # Check if correct password
    cursor.execute("SELECT email, firstname, lastname FROM User WHERE email=? AND password=?", [email, password])
    userMatch = cursor.fetchone()
    if(userMatch == None):
        return False

    # Sets currentUser to the logged in user
    global currentUser
    currentUser = {"email": userMatch[0], "firstName": userMatch[1], "lastName": userMatch[2]}
    return True
    

def view():
    cursor.execute("SELECT * FROM Roast")
    print(cursor.fetchall())

def review():
    # roastery, coffee name, points and notes
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")

    # Check if roast exists
    cursor.execute(f"SELECT * FROM Roast WHERE roastery = ? AND name = ?", [roastery, coffeeName])
    if(cursor.fetchone() == None):
        print("Could not find roast")
        return False

    #Check if points is an integer
    try:
        points = int(input("Points: "))
    except:
        print("Points must be an integer")
        return False
    notes = input("Notes: ")

    # Add to database    
    cursor.execute("INSERT INTO Tasting(userEmail, roastery, roastName, note, points, date) VALUES (?,?,?,?,?,?)",[currentUser["email"], roastery, coffeeName, notes, points, datetime.now()])
    con.commit()

def end():
    con.close()
    exit()

choices = {
    "v": view,
    "r": review,
    "e": end
}

def main():
    print("Welcome to CoffeeDB")
    while not login():
        print("Could not find user. Please try again")
    print(f"Welcome {currentUser['firstName']} {currentUser['lastName']}")
    
    while True:
        choice = ""
        while not choice in choices.keys():
            choice = input("What do you want to do?\n[v]iew coffees | add [r]eview | [e]nd program: ")
        choices[choice]()



main()
end()

