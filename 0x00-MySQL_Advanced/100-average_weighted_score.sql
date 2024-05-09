-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.

-- Requirements:

-- Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INTEGER)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
    DECLARE avg_weight DECIMAL(10, 2);
    SELECT AVG(weight) INTO avg_weight FROM corrections WHERE user_id = user_id;
    DECLARE avg_weighted_score DECIMAL(10, 2);
    SET avg_weighted_score = avg_score * avg_weight;
    UPDATE users SET average_score = avg_weighted_score WHERE id = user_id;
END $$
DELIMITER;
