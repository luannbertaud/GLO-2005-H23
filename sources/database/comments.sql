DROP TABLE IF EXISTS Comments;

CREATE TABLE IF NOT EXISTS Comments(
id INT AUTO_INCREMENT,
post INT NOT NULL,
sender VARCHAR(255) NOT NULL,
body TEXT NOT NULL,
timestamp DATETIME NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (post) REFERENCES Posts(id) ON DELETE CASCADE,
FOREIGN KEY (sender) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE SET NULL
);

