-- Creates a trigger that resets valid_email when email is changed
DELIMITER $$
CREATE TRIGGER reset_validation
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$
DELIMITER ;