ALTER TABLE category
RENAME TO categories


ALTER TABLE comments
ADD COLUMN post_id;

INSERT INTO 'comments' VALUES(NULL, 'what?', 'This was dang stupid gosh darnit!!', 'idk', 11/17/2020, 2)
