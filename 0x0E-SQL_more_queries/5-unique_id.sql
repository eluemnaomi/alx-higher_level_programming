-- Script creates table 'unique_id'
-- The id column is given constraints; 'DEFAULT' and 'UNIQUE'
CREATE TABLE  IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
