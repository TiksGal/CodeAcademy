# Parašyti programą, kuri:

# Atspausdintų dabartinę datą ir laiką
# Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# Patarimas: naudoti datetime, timedelta (from datetime import timedelta)

import datetime


laikas_dabar = datetime.datetime.now()
print(f"Dabartinė data ir laikas: {laikas_dabar}")
penkios_dienos_atgal = laikas_dabar - datetime.timedelta(days=5)
print(f"Dabartinė data ir laikas minus 5 dienos: {penkios_dienos_atgal}")
astuonios_valandos_pirmyn = laikas_dabar + datetime.timedelta(hours=8)
print(f"Dabartinė data ir laikas plius 8 valandos: {astuonios_valandos_pirmyn}")
x = laikas_dabar.strftime("%Y %m %d, %H:%M:%S")
print(f"Dabartinė data ir laikas formatu YYYY MM DD, HH:MM:SS: {x}")
