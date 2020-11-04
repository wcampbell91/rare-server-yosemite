import sqlite3
import json
from models import Comment

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
            c.post_id,
            c.creation_date
        FROM comments c
        """)

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'], row['post_id'])
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
            c.post_id,
            c.creation_date
        FROM comments c
        WHERE c.post_id = ?
        """, ( post_id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'], row['post_id'])
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
            c.post_id,
            c.creation_date
        FROM comments c
        WHERE c.id = ?
        """, ( id, ))

        comments = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            comment = Comment(row['id'], row['subject'], row['content'], row['author'], row['post_id'])
            comments.append(comment.__dict__)
            
    return json.dumps(comments)
