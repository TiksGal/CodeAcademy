import hashlib
import binascii
import os
import sqlite3
import msvcrt
from typing import Tuple, Union

def pbkdf2(password: str, salt: bytes, iterations: int, dklen: int) -> bytes:
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen)

def generate_salt() -> bytes:
    return os.urandom(16)

def encode_password(password: str, salt: bytes, iterations: int = 10000, dklen: int = 32) -> str:
    derived_key = pbkdf2(password, salt, iterations, dklen)
    return binascii.hexlify(derived_key).decode()

def create_database(db_name: str) -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            encoded_password TEXT NOT NULL,
            salt BLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user(db_name: str, username: str, password: str) -> None:
    salt = generate_salt()
    encoded_password = encode_password(password, salt)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (username, encoded_password, salt) VALUES (?, ?, ?)
    """, (username, encoded_password, salt))
    conn.commit()
    conn.close()

def authenticate_user(db_name: str, username: str, password: str) -> bool:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT encoded_password, salt FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if not result:
        return False

    encoded_password, salt = result
    test_encoded_password = encode_password(password, salt)

    return test_encoded_password == encoded_password

def windows_getpass(prompt: str) -> str:
    print(prompt, end="", flush=True)
    buf = b""
    while True:
        ch = msvcrt.getch()
        if ch in {b"\r", b"\n"}:
            break
        elif ch == b"\x08":  # Backspace
            buf = buf[:-1]
            print("\b \b", end="", flush=True)
        else:
            buf += ch
            print("*", end="", flush=True)
    print()
    return buf.decode()


def test_pbkdf2(db_name: str) -> None:
    username = input("Įveskite vartotojo vardą: ")
    password = windows_getpass("Įveskite slaptažodį: ")

    create_database(db_name)
    add_user(db_name, username, password)

    print("Vartotojas su užkoduotu slaptažodžiu pridėtas į duomenų bazę.")

    # Autentifikacijos testas
    test_username = input("Įveskite vartotojo vardą autentifikavimui: ")
    test_password = windows_getpass("Įveskite slaptažodį autentifikavimui: ")

    is_authenticated = authenticate_user(db_name, test_username, test_password)

    if is_authenticated:
        print("Autentifikacija sėkminga.")
    else:
        print("Autentifikacija nepavyko.")

if __name__ == "__main__":
    db_name = "users.db"
    test_pbkdf2(db_name)


