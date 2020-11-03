CREATE TABLE 'posts'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `title`   TEXT NOT NULL,
      `content`   TEXT NOT NULL,
      `category`  TEXT NOT NULL,
      `header_img` TEXT NOT NULL,
      `publish_date` TEXT NOT NULL
);

CREATE TABLE 'catergory'  (
      `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      `name`   TEXT NOT NULL,
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

CREATE TABLE 'post_tag' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'post_id' INTEGER NOT NULL, 
    'tag_id' INTEGER NOT NULL,
    FOREIGN KEY('post_id') REFERENCES 'posts'('id'),
    FOREIGN KEY('tag_id') REFERENCES 'tags'('id')
);