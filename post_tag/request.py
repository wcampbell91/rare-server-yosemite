import sqlite3
import json
from models import Post_tag

def create_post_tag(new_object):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        # new_object[post_id], new_object['tag_id']= []

        db_cursor.execute("""
            DELETE FROM post_tag
            WHERE post_id = ?
        """, (new_object['post_id'], ))

        params = []
        cmd = """
            INSERT INTO post_tag
                (post_id, tag_id)
            VALUES 
                (?, ?)
            """

        for tag in new_object['tag_id']:
            params.append((new_object['post_id'], tag))

        db_cursor.executemany(cmd, params)
