# Delivery 2: The Coffee database implemented in Python using SQLite

## Usage
The program is located in `program.py`. The program assumes `coffeDB.db` exists with the correct tables. 

If `coffeDB.db` is corrupted or missing, it can be generated with `createTables.py`. Additionally, the program `fillExampleData.py` can be run to fill the database with example data (Some of which is required for the user stories).

When running `program.py`, you will be presented with a login screen:

```
Welcome to CoffeeDB
Email: 
```

An example user exists with these credentials:

```
Welcome to CoffeeDB
Email: ola@normann.no
Password: besteOla123
```

After logging in successfully you will be presented with the following text:

```
Welcome Ola Normann
What do you want to do?
see most [v]alued coffees | add [t]asting | view [u]sers | search [d]escription | [f]ilter coffees on location and method | [e]nd program:
```

You will now be logged in as Ola Normann. To select an option, enter the character marked in brackets and press enter

## User stories

### 1 Adding a tasting
To add a tasting, start by entering `t` on the main menu. There you will get presented with some input fields. If you have loaded the example data provided you can enter the following for the tasting

```
Roastery: Trondheim brewery Jacobsen & Svart
Coffee Name: Vinterkaffe 2022
Points: 10
Notes: Wow - an odyssey for the taste buds: citrus peel, milk chocolate, apricot!
```
Now you have added a new tasting from Ola Normann

### 2 See who has tasted the most unique coffees this year

To see who has tasted the most coffees this year, simply enter `u` from the main menu. If you have loaded the exaple data, you will get either of these outputs:
- If you have not done user story 1
```
Users with tastings
===================
Ola Normann: 2 tastings
Per Kilo: 1 tasting
```
- If you have done user story 1
```
Users with tastings
===================
Ola Normann: 1 tasting
Per Kilo: 1 tasting
```

### 3 See the coffees with the highest value

To see the cofeess with the highest value, enter `v` in the main menu. If you have loaded the example data, you will get this output:
```
Most valued coffees
===================
Roast:Oksana 2019
Roastery: Walulu
Price: 200
Average score: 9.0
-----------------------
Roast:Vinterkaffe 2022
Roastery: Trondheim brewery Jacobsen & Svart
Price: 600
Average score: 5.0
-----------------------
```

### 4 Search descriptions

To search the user and roastery descriptions of the coffees for a special phrase, enter `f` in the main menu. Then you will get the following prompt:

```
A roast is described as:
```

Here you can for example enter
```
A roast is described as: floral
```

To get the following result (if you have loaded the example data)

```
Coffees described as floral
===========================
Roast: Oksana 2019
Roastery: Walulu
---------------
```

### 5 Filter based on countries and processing methods