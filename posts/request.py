from sqlite3
import json
from models import posts

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
        new_entry['id'] = id
      
    return json.dumps(new_post)
