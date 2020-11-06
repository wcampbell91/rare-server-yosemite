import sqlite3
import json
from models import User

def get_all_users():
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        cmd = """
        SELECT 
            u.id,
            u.name,
            u.avatar,
            u.display_name,
            u.email,
            u.creation_date,
            u.user_type,
            u.password
        FROM users u
        """
        db_cursor.execute(cmd)
        
        users = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            user = User(row['id'], row['name'], row['avatar'], row['display_name'], row['email'], row['creation_date'], row['user_type'], row['password'])
            users.append(user.__dict__)

        return json.dumps(users)


def get_single_user(id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        cmd = """
        SELECT
            u.id,
            u.name,
            u.avatar,
            u.display_name,
            u.email,
            u.creation_date,
            u.user_type,
            u.password
        FROM users u
        WHERE u.id = ?
        """
        params = (id, )

        db_cursor.execute(cmd, params)

        data = db_cursor.fetchone()

        user = User(data['id'], data['name'], data['avatar'], data['display_name'], data['email'], data['creation_date'], data['user_type'], data['password'])

        return json.dumps(user.__dict__)
