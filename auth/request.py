import sqlite3
import json
from models import User

def validate_user_login(user):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        cmd = """SELECT id FROM users WHERE email = ? AND password = ?"""
        params = (user['email'], user['password'], )

        db_cursor.execute(cmd, params)
        response = db_cursor.fetchone()

        if response is not None:
            return json.dumps(
            {
                "response": True,
                "user_id": response[0]
            })
        else:
            return json.dumps({"response": False})

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

        return json.dumps(user)
