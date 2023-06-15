import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    darbuotojai (
    vardas text,
    pavarde text,
    atlyginimas integer
    )""")

while True:
    print("Įveskite darbuotoją")
    vardas = input("Vardas: ")
    pavarde = input("Pavarde:")
    atlyginimas = int(input("atlyginimas :"))

    with conn:
        c.execute(f"INSERT INTO darbuotojai VALUES ('{vardas}', '{pavarde}', {atlyginimas})")

    with conn:
        c.execute("SELECT * FROM darbuotojai")
        print(c.fetchall())