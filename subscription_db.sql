CREATE DATABASE subscription_db;

USE subscription_db;

CREATE TABLE Users (
	user_id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(50),
	birthday DATE
);

CREATE TABLE Subs (
	sub_id INT AUTO_INCREMENT PRIMARY KEY,
	company_name VARCHAR(80),
	cost INT,
	sub_type VARCHAR(20),
	sub_time VARCHAR(20)
	
);

CREATE TABLE UserSub (
	user_id INT,
	sub_id INT,
	renewal_date DATE,
	pay_type VARCHAR(20),
	FOREIGN KEY (user_id) REFERENCES Users (user_id),
	FOREIGN KEY (sub_id) REFERENCES  Subs (sub_id)
);


CREATE TABLE renewal_notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    notification_date DATE,
    message TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);


DELIMITER //

CREATE TRIGGER SubscriptionRenewalReminder
AFTER UPDATE ON UserSub
FOR EACH ROW
BEGIN
    DECLARE days_until_renewal INT DEFAULT 7;


    IF DATEDIFF(NEW.renewal_date, CURDATE()) = days_until_renewal THEN

        INSERT INTO renewal_notifications (user_id, notification_date, message)
        VALUES (NEW.user_id, CURDATE(), 
                CONCAT('Reminder: Your subscription to ', (SELECT company_name FROM Subs WHERE sub_id = NEW.sub_id), 
                       ' will renew on ', NEW.renewal_date, '.'));
    END IF;
END //

DELIMITER ;
-- Make a trigger that alerts when a sub is more than 10% of monthly income.--
