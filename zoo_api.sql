CREATE DATABASE zoo_api;
USE zoo_api;

CREATE TABLE animal_table (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(100)NOT NULL,
    species VARCHAR(100)NOT NULL,
    special_requirements VARCHAR(100) NOT NULL
);

CREATE TABLE employee_table (
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(100) NOT NULL,
    schedule VARCHAR(100)NOT NULL
);

SELECT * FROM animal_table;
SELECT * FROM employee_table;
INSERT INTO employee_table (name, role, schedule)
VALUES ('aria', 'nurse', 'night');
ALTER TABLE employee_table
MODIFY COLUMN role VARCHAR(100) NOT NULL;


CREATE TABLE employee_register_table (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);