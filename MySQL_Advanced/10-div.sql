-- Creates a function that safely divides two numbers
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    -- Return 0 if b is 0 to avoid division by zero
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END$$
DELIMITER ;