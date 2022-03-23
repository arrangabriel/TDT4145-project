import sqlite3
con = sqlite3.connect("coffeeDB.db")
cursor = con.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS User (
    email varchar(255) NOT NULL PRIMARY KEY,
    password varchar(255),
    firstname varchar(255),
    lastname varchar(255)
)''') 

cursor.execute('''
CREATE TABLE IF NOT EXISTS Tasting (
    userEmail varchar(255) NOT NULL,
    roastery varchar(255) NOT NULL,
    roastName varchar(255) NOT NULL,
    note text(65,535),
    points int,
    date date,
    PRIMARY KEY (userEmail, roastery, roastName),
    FOREIGN KEY (userEmail) REFERENCES User(email),
    FOREIGN KEY (roastery) REFERENCES Roast(email),
    FOREIGN KEY (roastName) REFERENCES Roast(name)
); ''')

cursor.execute('''CREATE TABLE Roast (
    roastery varchar(255) NOT NULL,
    degree varchar(255) NOT NULL,
    date date,
    name varchar(255),
    description text(65,535),
    price int,
    batchID int,
    PRIMARY KEY (roastery, degree),
    FOREIGN KEY (batchID) REFERENCES Batch(batchID)
);''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Batch (
    batchID Integer PRIMARY KEY,
    price int,
    year int,
    note text(65,535),
    processingMethod varchar(255),
    farmID int,
    FOREIGN KEY (farmID) REFERENCES Farm(farmID),
    FOREIGN KEY (processingMethod) REFERENCES ProcessingMethod(name)
); ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ProcessingMethod (
    name varchar(255) NOT NULL PRIMARY KEY,
    description text(65,535)
);''') 

cursor.execute('''CREATE TABLE IF NOT EXISTS Farm (
    farmID Integer PRIMARY KEY,
    name varchar(255),
    country varchar(255),
    region varchar(255),
    masl int
);''') 

cursor.execute('''CREATE TABLE IF NOT EXISTS BatchBean (
    batchID int NOT NULL,
    beanName varchar(255) NOT NULL,
    beanSpecies varchar(255),
    PRIMARY KEY (batchID, beanName)
    FOREIGN KEY (beanName) REFERENCES Batch(batchID)
);''')
con.commit()
con.close()