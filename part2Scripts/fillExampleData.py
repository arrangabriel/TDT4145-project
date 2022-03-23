import sqlite3
con = sqlite3.connect("test.db")
cursor = con.cursor()
cursor.execute('''INSERT INTO User VALUES ('ola@normann.no', 'besteOla123', 'Ola', 'Normann')''')
cursor.execute('''INSERT INTO Farm VALUES (1, "Nombre de Dios", "El Salvador", "Santa Ana", 1500)''')
cursor.execute('''INSERT INTO ProcessingMethod VALUES ("washed", "The coffe has been washed")''')
cursor.execute('''INSERT INTO Batch VALUES (1, 8, 2021, "Fair Trade coffee from the beautiful Nombre de Dios", "washed", 1)''')
cursor.execute('''INSERT INTO BatchBean VALUES (1, "Bourbon", "coffea arabica")''')
cursor.execute('''INSERT INTO Roast VALUES ("Trondheim brewery Jacobsen & Svart", "light roast", '2022-01-20 00:00:00', "Vinterkaffe 2022", "A tasty and complex coffee for polar nights", 600, 1)''')
con.commit()
con.close()