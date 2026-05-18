import sqlite3
import hashlib

# DATABASE CONNECTION
conn = sqlite3.connect(
    "users.db",
    check_same_thread=False
)

cursor = conn.cursor()

# CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

conn.commit()

# HASH PASSWORD
def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()

# CREATE USER
def create_user(username, password):

    hashed_password = hash_password(
        password
    )

    cursor.execute(
        """
        INSERT INTO users
        (username, password)
        VALUES (?, ?)
        """,
        (username, hashed_password)
    )

    conn.commit()

# LOGIN USER
def login_user(username, password):

    hashed_password = hash_password(
        password
    )

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,
        (username, hashed_password)
    )

    return cursor.fetchone()