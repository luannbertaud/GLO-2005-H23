DROP TABLE IF EXISTS Follows;

CREATE TABLE IF NOT EXISTS Follows(
follower VARCHAR(255) NOT NULL,
followed VARCHAR(255) NOT NULL,
PRIMARY KEY(follower, followed),
FOREIGN KEY (follower) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY (followed) REFERENCES Users(username) ON UPDATE CASCADE ON DELETE CASCADE,
);
