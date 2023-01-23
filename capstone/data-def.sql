CREATE DATABASE capstone;

\c capstone; # Re-enter password

CREATE TABLE address (
    ID SERIAL PRIMARY KEY,
    Address VARCHAR(50),
    City VARCHAR(25),
    State VARCHAR(25),
    ZipCode VARCHAR(5)
);

CREATE TABLE customer (
    ID SERIAL PRIMARY KEY,
    FirstName VARCHAR(25),
    LastName VARCHAR(25),
    AddressID INT REFERENCES address(ID),
    Email VARCHAR(50)
);

CREATE TABLE account (
    ID SERIAL PRIMARY KEY,
    AccountNumber VARCHAR(10),
    CustomerID INT REFERENCES customer(ID),
    CurrentBalance FLOAT
);