import this
import datetime

# Sukurti failą "Tekstas.txt" ir įrašyti gautą tekstą į jį
with open("Tekstas.txt", "w") as f:
    f.write(this.s)

# Atspausdinti tekstą iš failo
with open("Tekstas.txt", "r") as f:
    print(f.read())

# Pridėti šiandienos datą ir laiką paskutinėje eilutėje
with open("Tekstas.txt", "a") as f:
    now = datetime.datetime.now()
    f.write("\n" + now.strftime("%Y-%m-%d %H:%M:%S"))

# Sunumeruoti teksto eilutes
with open("Tekstas.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for i, line in enumerate(lines, 1):
        f.write(f"{i}. {line}")
    f.truncate()

# Pakeisti teksto eilutę
with open("Tekstas.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if "Beautiful is better than ugly." in line:
            line = line.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")
        f.write(line)
    f.truncate()

# Atspausdinti tekstą atbulai
with open("Tekstas.txt", "r") as f:
    text = f.read()
    print(text[::-1])

# Suskaičiuoti žodžius, skaičius ir raidžių kiekius
with open("Tekstas.txt", "r") as f:
    text = f.read()
    word_count = len(text.split())
    number_count = sum(c.isdigit() for c in text)
    uppercase_count = sum(c.isupper() for c in text)
    lowercase_count = sum(c.islower() for c in text)
    print(f"Žodžių skaičius: {word_count}")
    print(f"Skaičių skaičius: {number_count}")
    print(f"Didžiųjų raidžių skaičius: {uppercase_count}")
    print(f"Mažųjų raidžių skaičius: {lowercase_count}")

# Nukopijuoti tekstą į naują failą didžiosiomis raidėmis
with open("Tekstas.txt", "r") as f:
    text = f.read()
    with open("Tekstas_didziosiomis.txt", "w") as new_file:
        new_file.write(text.upper())
