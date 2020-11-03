import sqlite3
import json
from models import Post

def create_post(new_post):
    with sqlite3.connect('../rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO posts
            (title, content, category_id, header_img)
        VALUES
            (?, ?, ?, ?)
        """, (new_post['title'], new_post['content'], new_post['category_id'], new_post['header_img']))

        id = db_cursor.lastrowid
        new_post['id'] = id
      
    return json.dumps(new_post)


def get_all_posts():
    with sqlite3.connect('../rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          p.id,
          p.title,
          p.content,
          p.category_id,
          p.header_img
        FROM posts p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
          post = Post(row['id'], row['title'], row['content'], row['category_id'], row['header_img'])
          posts.append(post.__dict__)

    return json.dumps(posts)
