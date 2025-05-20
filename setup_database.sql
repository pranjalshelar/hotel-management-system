CREATE DATABASE IF NOT EXISTS management;
USE management;


CREATE TABLE IF NOT EXISTS register (
    Fname VARCHAR(45),
    Lname VARCHAR(45),
    Contact VARCHAR(45),
    Email VARCHAR(45) PRIMARY KEY,
    SecurityQ VARCHAR(45),
    SecurityA VARCHAR(45),
    Password VARCHAR(45)
);


CREATE TABLE IF NOT EXISTS customer (
    Ref INT PRIMARY KEY,
    Name VARCHAR(45),
    DOB VARCHAR(40),
    Occupation VARCHAR(45),
    Gender VARCHAR(10),
    PostCode VARCHAR(10),
    Mobile VARCHAR(10),
    Email VARCHAR(45),
    Nationality VARCHAR(25),
    Idproof VARCHAR(20),
    IdNumber VARCHAR(45),
    Address VARCHAR(45)
);


CREATE TABLE IF NOT EXISTS room (
    Contact VARCHAR(45),
    Check_in VARCHAR(15),
    Check_out VARCHAR(15),
    Roomtype VARCHAR(45),
    Room VARCHAR(45) PRIMARY KEY,
    Meal VARCHAR(45),
    NoOfDays VARCHAR(45),
    Meal_Cost VARCHAR(45),
    Total_Bill VARCHAR(45),
    Payment_Mode VARCHAR(45)
);


CREATE TABLE IF NOT EXISTS details (
    Floor VARCHAR(45),
    RoomNo VARCHAR(45) PRIMARY KEY,
    RoomType VARCHAR(45)
);

INSERT INTO details (roomno, roomtype, status) VALUES
('101', 'Single', 'Available'),
('102', 'Single', 'Available'),
('201', 'Double', 'Available'),
('202', 'Double', 'Available'),
('301', 'Luxury', 'Available'),
('302', 'Luxury', 'Available'); 