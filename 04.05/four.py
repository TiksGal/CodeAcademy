import pickle

# Nuskaityti sąrašą iš pickle failo
try:
    with open("sarasas.pickle", "rb") as f:
        sarasas = pickle.load(f)
except FileNotFoundError:
    sarasas = []

# Pridėti pajamas arba išlaidas į sąrašą
while True:
    ivestis = input("Įveskite pajamas arba išlaidas (su '-' ženklu): ")
    if not ivestis:
        break
    sarasas.append(ivestis)

# Išsaugoti sąrašą pickle faile
with open("sarasas.pickle", "wb") as f:
    pickle.dump(sarasas, f)

# Atvaizduoti jau įvestas pajamas ir išlaidas
print("Jau įvesta:")
for ivestis in sarasas:
    print(ivestis)

# Atvaizduoti balansą
balansas = 0
for ivestis in sarasas:
    balansas += int(ivestis)
print(f"Balansas: {balansas}")
