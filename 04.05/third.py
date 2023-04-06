import os
import datetime

# Sukurti katalogą "Naujas Katalogas"
dir_name = "Naujas Katalogas"
desktop_path = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")
dir_path = os.path.join(desktop_path, dir_name)
os.makedirs(dir_path, exist_ok=True)

# Sukurti tekstinį failą su šiandienos data ir laiku
file_name = f"{datetime.date.today().strftime('%Y-%m-%d')} {datetime.datetime.now().strftime('%H-%M-%S')}.txt"
file_path = os.path.join(dir_path, file_name)
with open(file_path, "w") as f:
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# Atspausdinti tekstinio failo sukūrimo datą ir dydį baitais
file_stats = os.stat(file_path)
file_size = file_stats.st_size
file_creation_time = datetime.datetime.fromtimestamp(file_stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
print(f"Failo sukūrimo data: {file_creation_time}")
print(f"Failo dydis baitais: {file_size}")
