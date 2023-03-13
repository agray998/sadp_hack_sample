CREATE DATABASE IF NOT EXISTS qommon;
USE qommon;

CREATE TABLE driver (
    id INT PRIMARY KEY AUTO_INCREMENT,
    forename VARCHAR(20),
    surname VARCHAR(20)
);

CREATE TABLE package (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(50) NOT NULL,
    volume FLOAT NOT NULL,
    status VARCHAR(10),
    driver_id INT NOT NULL,
    FOREIGN KEY (driver_id) REFERENCES driver(id)
);