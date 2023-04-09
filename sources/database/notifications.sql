DROP TABLE IF EXISTS Notifications;

CREATE TABLE IF NOT EXISTS Notifications(
id INT NOT NULL,
type ENUM('like', 'comment', 'follow') NOT NULL,
body TEXT NOT NULL,
status ENUM('unread', 'read') NOT NULL,
PRIMARY KEY(id, type),
FOREIGN KEY(id) REFERENCES (...) ON UPDATE CASCADE ON DELETE CASCADE
);
