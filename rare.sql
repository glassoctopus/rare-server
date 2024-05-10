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

INSERT INTO posts (id, user_id,category_id,title,publication_date,image_url,content,approved)
VALUES (1,1232,112223,09809,"Hello World",02/02/2024,"dasdasd","sadasdsad",true);