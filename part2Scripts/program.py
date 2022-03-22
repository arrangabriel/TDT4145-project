import sqlite3
con = sqlite3.connect("test.db")
cursor = con.cursor()
currentUser = ""

def login():
    email = input("Email: ")
    password = input("Password: ")
    
    # Check if correct password
    cursor.execute(f"SELECT * FROM User WHERE email='{email}' AND password='{password}'")
    userMatch = cursor.fetchone()
    if(userMatch == None):
        return False

    # Sets currentUser to the logged in user
    global currentUser
    currentUser = userMatch
    return True
    

def view():
    cursor.execute("SELECT * FROM Roast")
    print(cursor.fetchall())

def review():
    # roastery, coffee name, points and notes
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    points = int(input("Points: "))
    notes = input("Notes: ")

    # Check if roast exists
    cursor.execute(f"SELECT * FROM Roast WHERE roastery = '{roastery}' AND name = '{coffeeName}")
    cursor.execute(f"")

def main():
    print("Welcome to")
    while not login():
        print("Could not find user. Please try again")
    print(f"Welcome")
    choices = {
        "v": view,
        "r": review
    }
    choice = ""
    while not choice in choices.keys():
        choice = input("What do you want to do?\n[v]iew coffees | add [r]eview: ")
    choices[choice]()

def end():
    con.close()
    exit()

main()
end()

