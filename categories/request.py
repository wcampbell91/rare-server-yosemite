import sqlite3
import json

def get_all_categories():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
        FROM Categories a
        """)

        dataset = db_cursor.fetchall()

        for row in dataset:

            category = Categories(row['id'], row['name]) 
            
            categories.append(entry.__dict__)

    return json.dumps(categories)
