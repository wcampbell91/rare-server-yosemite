import sqlite3
import json
from models import Post
from datetime import datetime

def create_post(new_post):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO posts
            (title, content, category_id, header_img, user_id, publish_date)
        VALUES
            (?, ?, ?, ?, ?, ?)
        """, (new_post['title'], new_post['content'], new_post['category_id'], new_post['header_img'], new_post['user_id'], datetime.now()))

        id = db_cursor.lastrowid

        for tag in new_post['tags']:
            cmd = """INSERT INTO post_tag
                        (post_id, tag_id)
                    VALUES 
                        (?, ?)"""
            params = (id, tag)

            db_cursor.execute(cmd, params)

        new_post['id'] = id

    return json.dumps(new_post)


def get_all_posts():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          p.id,
          p.title,
          p.content,
          p.category_id,
          p.header_img,
          p.user_id,
          p.publish_date
        FROM posts p
        """)

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['category_id'], row['header_img'], row['user_id'], row['publish_date'])

            cmd = """SELECT t.id, t.name FROM post_tag pt
                    JOIN tags t ON t.id = pt.tag_id
                    WHERE pt.post_id = ?
                    """
            params = (post.id, )

            db_cursor.execute(cmd, params)

            tagset = db_cursor.fetchall()

            tags = []

            for tag in tagset:
                tags.append({
                    'id': tag['id'],
                    'name': tag['name'],
                })

            post.tags = tags

            posts.append(post.__dict__)

    return json.dumps(posts)

def get_posts_by_user(user_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.title,
            p.content,
            p.category_id,
            p.header_img,
            p.user_id,
            p.publish_date
        FROM posts p
        WHERE p.user_id = ?
        """, ( user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['category_id'], row['header_img'], row['user_id'], row['publish_date'])
            posts.append(post.__dict__)
    return json.dumps(posts)

def get_single_post(id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
          p.id,
          p.title,
          p.content,
          p.category_id,
          p.header_img,
          p.user_id,
          p.publish_date
        FROM posts p
        WHERE p.id = ?
        """, (id, ))

        posts = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['title'], row['content'], row['category_id'], row['header_img'], row['user_id'], row['publish_date'])
            posts.append(post.__dict__)
    return json.dumps(posts)

def update_post(id, new_post):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE posts
            SET
            title = ?,
            content = ?,
            category_id = ?,
            header_img = ?
        WHERE id = ?
        """, (new_post['title'], new_post['content'], new_post['category_id'], new_post['header_img'], id ))

    rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True

def delete_post(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM posts
        WHERE id = ?
        """, (id, ))
