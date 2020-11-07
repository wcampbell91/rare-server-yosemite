import sqlite3
import json
from models import User
from datetime import datetime

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

def create_user(new_user):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO users
            ( name, avatar, display_name, email, creation_date, user_type, password )
        VALUES
            (?, ?, ?, ?, ?, ?, ?)
        """, (new_user['name'], new_user['avatar'], 
                new_user['display_name'], new_user['email'], datetime.now(), new_user['user_type'], new_user['password'] ))
        id = db_cursor.lastrowid

        new_user['id'] = id

    return json.dumps(new_user)
