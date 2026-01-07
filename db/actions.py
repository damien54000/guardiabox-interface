from db.db import get_db

def log_action(user_id, action, format):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO history (user_id, action, format) VALUES (?, ?, ?)",
        (user_id, action, format)
    )

    conn.commit()
    conn.close()
