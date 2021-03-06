DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS post_tag;

CREATE TABLE 'posts'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `title`   TEXT NOT NULL,
      `content`   TEXT NOT NULL,
      `category_id`  INTEGER NOT NULL,
      `header_img` TEXT NOT NULL
);

CREATE TABLE 'categories'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `name`   TEXT NOT NULL
);

CREATE TABLE 'tags'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `name`   TEXT NOT NULL
);

CREATE TABLE 'comments'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `subject`   TEXT NOT NULL,
      `content`   TEXT NOT NULL,
      `author`  TEXT NOT NULL,
      `creation_date` TEXT NOT NULL
);

CREATE TABLE 'users'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `name`   TEXT NOT NULL,
      `avatar`   TEXT NOT NULL,
      `display_name`  TEXT NOT NULL,
      `email` TEXT NOT NULL,
      `creation_date` TEXT NOT NULL,
      `user_type` TEXT NOT NULL
);

INSERT INTO 'users' VALUES(null, 'Butt Chugg', '23423', 'coolGuy123', 'chugg.butt@email.com', '223423', 'admin', 'password');

ALTER TABLE 'users'
ADD 'password' TEXT

CREATE TABLE 'post_tag' (
      'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      'post_id' INTEGER NOT NULL, 
      'tag_id' INTEGER NOT NULL,
      FOREIGN KEY('post_id') REFERENCES 'posts'('id'),
      FOREIGN KEY('tag_id') REFERENCES 'tags'('id')
);

ALTER TABLE comments
ADD post_id VARCHAR(65535);

INSERT INTO `categories` VALUES (NULL, 'TEST 1');
INSERT INTO `categories` VALUES(NULL, 'TEST 2');
INSERT INTO `categories` VALUES(NULL, 'TEST 3');
INSERT INTO `categories` VALUES(NULL, 'TEST 4');


INSERT INTO 'comments' VALUES(NULL, 'footballssss', 'here is a cool comment on football', 'idkbro', "11/17/2020", 1);
INSERT INTO 'comments' VALUES(NULL, 'indie', 'here is a cool comment on football', 'bro', "11/17/2020", 2);
INSERT INTO 'comments' VALUES(NULL, 'folk', 'here is a cool comment on football', 'idk', "11/17/2020", 3)
DELETE FROM comments WHERE id='5';


INSERT INTO 'tags' VALUES(null, 'politics')
INSERT INTO 'tags' VALUES(null, 'football')
INSERT INTO 'tags' VALUES(null, 'indie')
INSERT INTO 'tags' VALUES(null, 'folk')

IF EXISTS (SELECT * FROM users WHERE email = ? AND password = ?) THEN SELECT 'true' ELSE SELECT 'false' 
