CREATE TABLE User (
    email varchar(255) NOT NULL PRIMARY KEY,
    password varchar(255),
    firstname varchar(255),
    lastname varchar(255)
); 

CREATE TABLE Tasting (
    userEmail varchar(255) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES User(email),
    roastery varchar(255) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES Roast(roastery),
    roastName varchar(255) NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES Roast(name),
    note text(65,535),
    points int,
    date date
); 

CREATE TABLE Roast (
    roastery varchar(255) NOT NULL PRIMARY KEY,
    degree varchar(255) NOT NULL PRIMARY KEY,
    date date,
    name varchar(255),
    description text(65,535),
    price int,
    batchID int FOREIGN KEY REFERENCES Batch(roastID)
); 

CREATE TABLE Batch (
    batchID int NOT NULL PRIMARY KEY,
    price int,
    year int,
    note text(65,535),
    processingMethod varchar(255) FOREIGN KEY REFERENCES ProcessingMethod(name),
    farmID int FOREIGN KEY REFERENCES Farm(farmID)
); 

CREATE TABLE ProcessingMethod (
    note text(65,535) NOT NULL PRIMARY KEY,
    description text(65,535)
); 

CREATE TABLE Farm (
    farmID int NOT NULL PRIMARY KEY,
    name varchar(255),
    country varchar(255),
    region varchar(255),
    masl int
); 

CREATE TABLE BatchBean (
    batchID int NOT NULL PRIMARY KEY FOREIGN KEY REFERENCES Batch(batchID),
    beanName varchar(255) NOT NULL PRIMARY KEY
    beanSpecies varchar(255)
);