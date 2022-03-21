import sqlite3
con = sqlite3.connect("test.db")
cursor = con.cursor()


def view():
    cursor.execute("SELECT * FROM Roast")
    print(cursor.fetchall())

def review():
    # roastery, coffee name, points and notes
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")
    points = int(input("Points: "))
    notes = input("Notes: ")

def main():
    choices = {
        "v": view,
        "r": review
    }
    choice = ""
    while not choice in choices.keys():
        choice = input("What do you want to do?\n[v]iew coffees | add [r]eview: ")
    choices[choice]()
main()

con.close()