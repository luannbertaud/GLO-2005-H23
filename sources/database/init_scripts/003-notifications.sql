DROP TABLE IF EXISTS Notifications;

CREATE TABLE IF NOT EXISTS Notifications(
id INT NOT NULL,
type ENUM('like', 'comment', 'follow') NOT NULL,
status ENUM('unread', 'read') NOT NULL,
PRIMARY KEY(id, type)
);
