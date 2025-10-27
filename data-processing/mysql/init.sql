-- ===========================================
-- Initialization Script for Employee Database
-- ===========================================
CREATE DATABASE IF NOT EXISTS employee;
USE employee;

-- Create table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    join_date DATE,
    release_date DATE,
    years_of_experience INT,
    salary DECIMAL(10,2)
);

-- Insert dataset
INSERT INTO employees (name, position, join_date, release_date, years_of_experience, salary) VALUES
('Jacky', 'Solution Architect', '2018-07-25', '2022-07-25', 8, 150.00),
('John', 'Assistant Manager', '2016-02-02', '2021-02-02', 12, 155.00),
('Alano', 'Manager', '2010-11-09', NULL, 14, 175.00),
('Aaron', 'Engineer', '2021-08-16', '2022-08-16', 1, 80.00),
('Allen', 'Engineer', '2024-06-06', NULL, 4, 75.00),
('Peter', 'Team Leader', '2020-01-09', NULL, 3, 85.00);

-- Validate that the data is correctly loaded
SELECT * FROM employees;
