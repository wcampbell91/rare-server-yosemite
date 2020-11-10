import sqlite3
import json
from models import Tag, Post

def get_all_tags():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.name
        FROM tags t
        ORDER BY 
            name ASC
        """)

        tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            tag = Tag(row['id'], row['name'])

            tags.append(tag.__dict__)
    return json.dumps(tags)

def create_tag(new_tag):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()
        cmd = """
            INSERT INTO tags
                (name)
            VALUES
                (?)
            """
        params = (new_tag['name'], )

        db_cursor.execute(cmd, params)

        id = db_cursor.lastrowid

        new_tag['id'] = id

    return json.dumps(new_tag)

def delete_tag(id):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()
        cmd = """
        DELETE FROM tags
        WHERE id = ?
        """

        params = (id, )

        db_cursor.execute(cmd, params)

def update_tag(id, new_tag):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE tags
            SET
            name = ?
        WHERE id = ?
        """, (new_tag['name'], id))
    
    rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
