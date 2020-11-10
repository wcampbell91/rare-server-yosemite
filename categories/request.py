import sqlite3
import json
from models import Category

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name
        FROM categories a
        ORDER BY name ASC;
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row['id'], row['name'])
            
            categories.append(category.__dict__)
    return json.dumps(categories)

def create_category(new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO categories
            (name)
        VALUES
            (?);
        """, (new_category['name'], ))


        id = db_cursor.lastrowid

        new_category['id'] = id

    return json.dumps(new_category)

def delete_category(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id, ))

def update_category(id, new_category):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Categories
            SET
            Name = ?
        WHERE id = ?
        """, (new_category['name'], id ))

    rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
