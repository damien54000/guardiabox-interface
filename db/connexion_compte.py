from db.db import get_db
import hashlib


def login_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password_hash = ?",
        (username, password_hash)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        print("Connexion réussie")
        return row[0]  # user_id
    else:
        print("Identifiants incorrects")
        return None
