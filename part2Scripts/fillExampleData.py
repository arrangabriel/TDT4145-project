import sqlite3
con = sqlite3.connect("coffeeDB.db")
cursor = con.cursor()
# Users
cursor.execute('''INSERT INTO User VALUES ('ola@normann.no', 'besteOla123', 'Ola', 'Normann')''')
cursor.execute('''INSERT INTO User VALUES ('a', 'b', 'A', 'Mc. A')''')

# Farms
cursor.execute('''INSERT INTO Farm VALUES (1, "Nombre de Dios", "El Salvador", "Santa Ana", 1500)''')
cursor.execute('''INSERT INTO Farm VALUES (2, "Galdhøpiggen", "Norway", "Jotunheimen", 2469)''')


# Processing Methods
cursor.execute('''INSERT INTO ProcessingMethod VALUES ("washed", "The coffe has been washed")''')
cursor.execute('''INSERT INTO ProcessingMethod VALUES ("snowdried", "The coffe has been dried with the fines and purest snow from nordkapp")''')


# Batches
cursor.execute('''INSERT INTO Batch VALUES (1, 8, 2021, "Fair Trade coffee from the beautiful Nombre de Dios", "washed", 1)''')
cursor.execute('''INSERT INTO Batch VALUES (2, 3, 2019, "Good Batch", "washed", 2)''')


# Batch Beans
cursor.execute('''INSERT INTO BatchBean VALUES (1, "Bourbon", "coffea arabica")''')

# Roasts
cursor.execute('''INSERT INTO Roast VALUES ("Trondheim brewery Jacobsen & Svart", "light roast", '2022-01-20 00:00:00', "Vinterkaffe 2022", "A tasty and complex coffee for polar nights", 600, 1)''')
cursor.execute('''INSERT INTO Roast VALUES ("Walulu", "dark roast", '2022-02-20 00:00:00', "Oksana 2019", "your run of the mill rwandan dark roast", 200, 2)''')

#Tastings
cursor.execute('''INSERT INTO Tasting VALUES ("a", "Walulu", "Oksana 2019", "Tasted of pure snowy heaven", 10, "2022-03-5 00:00:21")''')
cursor.execute('''INSERT INTO Tasting VALUES ("a", "Trondheim brewery Jacobsen & Svart", "Vinterkaffe 2022", "Tasted of light heaven", 5, "2022-03-5 00:00:22")''')
cursor.execute('''INSERT INTO Tasting VALUES ("ola@normann.no", "Walulu", "Oksana 2019", "Tasted of good floral", 8, "2022-03-5 00:00:25")''')



con.commit()
con.close()
