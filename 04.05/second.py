line_count = int(input("Įveskite norimą eilučių kiekį: "))
filename = input("Įveskite norimą failo pavadinimą: ")

with open(filename, "w") as f:
    line_number = 1
    while line_number <= line_count:
        line = input(f"Įveskite {line_number}-ąją eilutę: ")
        if not line:
            break
        f.write(line + "\n")
        line_number += 1

print(f"Failas {filename} sukurtas.")

