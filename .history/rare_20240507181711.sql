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