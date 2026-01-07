from db.db import get_db
import hashlib
import sqlite3


def create_user(username, password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, password_hash)
        )
        conn.commit()
        print("Compte créé avec succès")
    except sqlite3.IntegrityError:
        print("Nom d'utilisateur déjà utilisé")

    conn.close()
