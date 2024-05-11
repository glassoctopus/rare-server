CREATE TABLE `Subscription` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `follower_id`    INTEGER NOT NULL,
    `author_id`    INTEGER NOT NULL,
    `created_on`    TEXT NOT NULL
);

CREATE TABLE `Category` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label`    TEXT NOT NULL
);

INSERT INTO comments (id, author_id,post_id,content)
VALUES (1,1232,112223,"Hello World");