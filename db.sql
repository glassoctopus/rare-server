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

INSERT INTO Users ('first_name', 'last_name', 'email', 'bio', 'username', 'password', 'profile_image_url', 'created_on', 'active') VALUES ('Sarah', 'Brown', 'user1@example.com', 'This is my bio.', 'User1', 'password1', 'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/330px-Original_Doge_meme.jpg', (CURRENT_DATE), 1)

CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

INSERT INTO Users ('first_name', 
                    'last_name', 
                    'email', 
                    'bio', 
                    'username', 
                    'password', 
                    'profile_image_url', 
                    'created_on', 
                    'active') VALUES ('Sarah', 
                                      'Brown', 
                                      'user1@example.com', 
                                      'This is my bio.', 
                                      'User1', 'password1', 
                                      'https://upload.wikimedia.org/wikipedia/en/thumb/5/5f/Original_Doge_meme.jpg/330px-Original_Doge_meme.jpg', 
                                      (CURRENT_DATE), 
                                      1)

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO POSTS ('user_id',
                      'category_id',
                      'title',
                      'publication_date',
                      'image_url',
                      'content',
                      'approved'
                      ) VALUES ('1',
                                '2',
                                'Ipsum Lorem',
                                'January 2024',
                                '',
                                'Latin Stuff',
                                True
                                )

INSERT INTO Subscriptions ('',
                            '',
                            '',
                            '') VALUES ('',
                                        '',
                                        '',
                                        '')




