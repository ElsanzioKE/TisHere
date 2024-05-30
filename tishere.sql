-- Prepares a MySQL server for the tisher project.
CREATE DATABASE IF NOT EXISTS tishere;
CREATE USER IF NOT EXISTS 'tishere_dev'@'localhost' IDENTIFIED BY 'tishere_pwd';
GRANT ALL PRIVILEGES ON tishere . * TO 'tishere_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'tishere_dev'@'localhost';