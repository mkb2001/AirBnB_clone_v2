-- CREATE NEW USER hbnb_test and SCHEMA hbnb_test_db in localhost
-- SET PRIVELEGES OF hbnb_test TO `ALL` ON hbnb_test_db and SELECT ON performance_schema
CREATE SCHEMA IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
