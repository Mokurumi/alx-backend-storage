-- Write a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.

-- Requirements:

-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - if no projects.name found in the table, you should create it
-- score, the score value for the correction

CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
    `id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `state_id` INT NOT NULL,
    `name` VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
