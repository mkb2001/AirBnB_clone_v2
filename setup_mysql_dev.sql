-- CREATES A NEW USER hbnb_dev AND DATABASE hbnb_dev_db
-- GRANTS ALL PRIVILEGES TO hbnb_dev ON hbnb_dev_db AND ONLY SELECT ON performance_schema
CREATE SCHEMA IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
