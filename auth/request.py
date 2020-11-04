import sqlite3
import json
from models import User

def validate_user_login(user):
    with sqlite3.connect('./rare.db') as conn:
        db_cursor = conn.cursor()

        cmd = """SELECT EXISTS ( SELECT * FROM users WHERE email = ? AND password = ?)"""
        params = (user['email'], user['password'], )

        db_cursor.execute(cmd, params)
        response = db_cursor.fetchone()

        if response[0] == 1:
            return json.dumps({"response": True})
        else:
            return json.dumps({"response": False})
