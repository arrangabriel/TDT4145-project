import sqlite3
from datetime import datetime

con = sqlite3.connect("coffeeDB.db")
cursor = con.cursor()
currentUser = None


def login() -> bool:
    email: str = input("Email: ")
    password: str = input("Password: ")

    # Check if correct password
    cursor.execute(
        """SELECT email, firstname, lastname
        FROM User
        WHERE email=? AND password=?""",
        [email, password])

    userMatch = cursor.fetchone()
    if(userMatch == None):
        return False

    # Sets currentUser to the logged in user
    global currentUser
    currentUser = {
        "email": userMatch[0],
        "firstName": userMatch[1],
        "lastName": userMatch[2],
    }
    return True


def tasting() -> bool:
    # roastery, coffee name, points and notes
    roastery = input("Roastery: ")
    coffeeName = input("Coffee Name: ")

    # Check if roast exists
    cursor.execute(
        """SELECT *
        FROM Roast
        WHERE roastery = ? AND name = ?""",
        [roastery, coffeeName])

    if(cursor.fetchone() == None):
        print("Could not find roast")
        return False

    # Check if points is an integer
    try:
        points = int(input("Points: "))
    except:
        print("Points must be an integer")
        return False
    notes = input("Notes: ")

    # Add to database
    cursor.execute(
        """INSERT INTO Tasting(email, roastery, roastName, note, points, date)
        VALUES (?,?,?,?,?,?)""",
        [currentUser["email"], roastery, coffeeName, notes, points, datetime.now().date()])

    con.commit()
    return True


def viewUsers() -> None:
    print("Users with tastings")
    print("===================")
    time = str(datetime.now().year) + '-01-01'
    cursor.execute(
        """SELECT COUNT(*) AS noTastings, email, firstname, lastname
        FROM Tasting
        NATURAL JOIN User
        WHERE date(Tasting.date) > date(?)
        GROUP BY email
        ORDER BY noTastings DESC""", [time])

    for user in cursor.fetchall():
        print(f"{user[2]} {user[3]}: {user[0]} tasting{'' if user[0] == 1 else 's'}")


def filter():
    countries = input(
        'Which countries would you like to see coffees from?\nProvide a comma separated list: ')
    c = [country.strip() for country in countries.split(',')]

    cursor.execute("""SELECT name
    FROM ProcessingMethod""")
    methods = cursor.fetchall()

    print("All processing methods: ")
    dictMethod = {}
    for i, method in enumerate(methods, start=1):
        print(str(i), ":", method[0])
        dictMethod[i] = method[0]
    dictMethod[0] = ''
    try:
        excludedProcessingMethod = int(input(
            'Which processing method do you want excluded (enter to include all): '))
    except:
        excludedProcessingMethod = 0
    # Please note that no user input is injected into the SQL query using the format string.
    # It is simply used to vary the amount of injection points, '?-marks', for cursor.execute.
    cursor.execute(
        f"""SELECT Roast.roastery, Roast.name
        FROM (SELECT c, p, b FROM 
        (SELECT Farm.country as c, Batch.processingMethod as p, Batch.batchID as b
        FROM Farm, Batch 
        WHERE Batch.farmID = Farm.farmID)
        WHERE p != ? AND c IN ({"?,"*(len(c)-1)}?))
        , Roast
        WHERE Roast.batchID = b""", [dictMethod[excludedProcessingMethod], *c])
    print("=====================")
    for coffee in cursor.fetchall():
        print(f"Roast: {coffee[1]}\nRoastery: {coffee[0]}")
        print("---------------")



def descibed():
    describedAs = input("A roast is described as: ")

    cursor.execute(
        """SELECT DISTINCT Roast.roastery, Roast.name
        FROM Roast INNER JOIN Tasting 
        ON Roast.name = Tasting.roastName AND Roast.roastery = Tasting.roastery
        WHERE Tasting.note LIKE ?
        """, ["%" + describedAs + "%", ])

    print(f"Coffees described as {describedAs}")
    print("=====================" + "=" * len(describedAs))
    for coffee in cursor.fetchall():
        print(f"Roast: {coffee[1]}\nRoastery: {coffee[0]}")
        print("---------------")


def values():
    print("Most valued coffees")
    print("===================")

    cursor.execute(
        """SELECT Roast.roastery, name, price, avg(points)
    FROM Tasting 
    INNER JOIN Roast ON Tasting.roastName = Roast.name AND Tasting.roastery = Roast.roastery
    GROUP BY Roast.name, Roast.roastery ORDER BY avg(points/price) DESC""")

    for coffee in cursor.fetchall():
        print(
            f"Roast:{coffee[1]}\nRoastery: {coffee[0]}\nPrice: {coffee[2]}\nAverage score: {coffee[3]}")
        print("-----------------------")


def end():
    con.close()
    exit()


choices = {
    "t": tasting,
    "u": viewUsers,
    "e": end,
    "v": values,
    "d": descibed,
    "f": filter,
}


def main():
    print("Welcome to CoffeeDB")
    while not login():
        print("Could not find user. Please try again")
    print(f"Welcome {currentUser['firstName']} {currentUser['lastName']}")

    while True:
        choice = ""
        while not choice in choices.keys():
            choice = input(
                "What do you want to do?\nsee most [v]alued coffees | add [t]asting | view [u]sers | search [d]escription | [f]ilter coffees on location and method | [e]nd program: ")
        choices[choice]()


main()
