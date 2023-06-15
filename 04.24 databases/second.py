import sqlite3

def main():
    conn = sqlite3.connect('paskaitos1.db')

    create_table(conn)
    insert_data(conn)
    print_lectures_longer_than(conn, 50)
    update_python_lecture(conn)
    delete_tomas_lecture(conn)
    print_all_lectures(conn)

    conn.close()

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS paskaitos (
            pavadinimas TEXT,
            destytojas TEXT,
            trukme INTEGER
        )
    """)
    conn.commit()

def insert_data(conn):
    cursor = conn.cursor()
    lectures = [
        ('Vadyba', 'Domantas', 40),
        ('Python', 'Donatas', 80),
        ('Java', 'Tomas', 80)
    ]
    cursor.executemany("""
        INSERT INTO paskaitos (pavadinimas, destytojas, trukme)
        VALUES (?, ?, ?)
    """, lectures)
    conn.commit()

def print_lectures_longer_than(conn, duration):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM paskaitos WHERE trukme > ?
    """, (duration,))
    lectures = cursor.fetchall()
    print("Paskaitos, kurių trukmė didesnė už 50:")
    for lecture in lectures:
        print(lecture)

def update_python_lecture(conn):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE paskaitos
        SET pavadinimas = 'Python programavimas'
        WHERE pavadinimas = 'Python'
    """)
    conn.commit()

def delete_tomas_lecture(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM paskaitos WHERE destytojas = 'Tomas'
    """)
    conn.commit()

def print_all_lectures(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM paskaitos")
    lectures = cursor.fetchall()
    print("Visos paskaitos:")
    for lecture in lectures:
        print(lecture)

if __name__ == '__main__':
    main()
