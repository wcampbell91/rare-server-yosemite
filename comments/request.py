import sqlite3
import json
from sqlite3.dbapi2 import connect
from models import Comment
from datetime import datetime

def get_all_comments():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.subject,
            c.content,
            c.author,
            c.creation_date,
            c.post_id
            
        FROM comments c
        """)

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'],row['creation_date'], row['post_id'] )
            comments.append(comment.__dict__)

    return json.dumps(comments)

def get_all_comments_by_post_id(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.subject,
            c.content,
            c.author,
            c.creation_date,
            c.post_id
            
        FROM comments c
        WHERE c.post_id = ?
        """, ( post_id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'],row['creation_date'], row['post_id'])
            comments.append(comment.__dict__)
            
    return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.subject,
            c.content,
            c.author,
            c.creation_date,
            c.post_id
            
        FROM comments c
        WHERE c.id = ?
        """, ( id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'],row['creation_date'], row['post_id'])
            comments.append(comment.__dict__)
            
    return json.dumps(comments)

def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO comments
            (subject, content, author, creation_date, post_id)
        VALUES
            (?, ?, ?, ?, ?);
        """, ( new_comment['subject'], new_comment['content'], new_comment['author'],datetime.now(), new_comment['post_id'], ))


        id = db_cursor.lastrowid

        new_comment['id'] = id

    return json.dumps(new_comment)

def delete_comments(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET
            subject = ?,
            content = ?,
            author = ?,
            creation_date = ?,
            post_id = ?

        WHERE id = ?
        """, (new_comment['subject'], new_comment['content'],new_comment['author'],new_comment['creation_date'], new_comment['post_id'], id ))

    rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
