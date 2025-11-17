import os
import re

# Pfad anpassen
folder = r"C:\Projects\werkstatt\img\all\original\garderobe"

# Gültige Bild-Endungen
valid_extensions = (".jpg", ".jpeg", ".png", ".heic")

# Nur Bilder mit Zahlen im Namen erfassen und numerisch sortieren
def extract_number(filename):
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')

# Bilderliste
images = [f for f in os.listdir(folder) if f.lower().endswith(valid_extensions)]
images.sort(key=extract_number)  # numerisch aufsteigend sortieren

# Umbenennen in 0.jpg, 1.jpg, 2.jpg ...
for i, filename in enumerate(images):
    _, ext = os.path.splitext(filename)
    new_name = f"{i}{ext.lower()}"
    src = os.path.join(folder, filename)
    dst = os.path.join(folder, new_name)

    if os.path.exists(dst):
        temp_name = os.path.join(folder, f"__temp_{i}{ext.lower()}")
        os.rename(src, temp_name)
    else:
        os.rename(src, dst)

# 2. Durchgang für temporäre Dateien
for filename in os.listdir(folder):
    if filename.startswith("__temp_"):
        number = filename.split("_")[-1]
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, number)
        os.rename(src, dst)

print("✅ Bilder wurden numerisch umbenannt.")
