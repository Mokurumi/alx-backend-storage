-- Write a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.

-- Requirements:

-- Procedure ComputeAverageWeightedScoreForUsers is not taking any input.

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INTEGER;
    DECLARE done INTEGER DEFAULT 0;
    DECLARE avg_score DECIMAL(10, 2);
    DECLARE avg_weight DECIMAL(10, 2);
    DECLARE avg_weighted_score DECIMAL(10, 2);
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT AVG(score) INTO avg_score FROM corrections WHERE user_id = user_id;
        SELECT AVG(weight) INTO avg_weight FROM corrections WHERE user_id = user_id;
        SET avg_weighted_score = avg_score * avg_weight;
        UPDATE users SET average_score = avg_weighted_score WHERE id = user_id;
    END LOOP;
    CLOSE cur;
END $$
DELIMITER;
