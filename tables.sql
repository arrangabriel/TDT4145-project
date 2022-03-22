CREATE TABLE User (
    email varchar(255) NOT NULL PRIMARY KEY,
    password varchar(255),
    firstname varchar(255),
    lastname varchar(255)
); 

CREATE TABLE Tasting (
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
); 

CREATE TABLE Roast (
    roastery varchar(255) NOT NULL,
    degree varchar(255) NOT NULL,
    date date,
    name varchar(255),
    description text(65,535),
    price int,
    batchID int,
    PRIMARY KEY (roastery, name),
    FOREIGN KEY (batchID) REFERENCES Batch(batchID)
); 

CREATE TABLE Batch (
    batchID Integer PRIMARY KEY,
    price int,
    year int,
    note text(65,535),
    processingMethod varchar(255),
    farmID int,
    FOREIGN KEY (farmID) REFERENCES Farm(farmID),
    FOREIGN KEY (processingMethod) REFERENCES ProcessingMethod(name)
); 

CREATE TABLE ProcessingMethod (
    name varchar(255) NOT NULL PRIMARY KEY,
    description text(65,535)
); 

CREATE TABLE Farm (
    farmID Integer PRIMARY KEY,
    name varchar(255),
    country varchar(255),
    region varchar(255),
    masl int
); 

CREATE TABLE BatchBean (
    batchID int NOT NULL,
    beanName varchar(255) NOT NULL,
    beanSpecies varchar(255),
    PRIMARY KEY (batchID, beanName)
    FOREIGN KEY (beanName) REFERENCES Batch(batchID)
);