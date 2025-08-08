import os
import subprocess
from PIL import Image

# Deine Pfade
input_dir = 'img/all/original'
output_dir = 'img/all/edited'
max_size = (1600, 1600)

# Ausgabeordner erstellen, falls nicht vorhanden
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    name, ext = os.path.splitext(filename)
    input_path = os.path.join(input_dir, filename)
    temp_jpg_path = os.path.join(output_dir, f"{name}_converted.jpg")
    final_jpg_path = os.path.join(output_dir, f"{name}.jpg")

    # Nur Bilddateien verarbeiten
    if ext.lower() == ".heic":
        print(f"🔄 Konvertiere HEIC: {filename}")
        subprocess.run(["magick", input_path, temp_jpg_path], check=True)

        with Image.open(temp_jpg_path) as img:
            img.thumbnail(max_size)
            img.convert("RGB").save(final_jpg_path, "JPEG", quality=85)
        os.remove(temp_jpg_path)

    elif ext.lower() in [".jpg", ".jpeg", ".png"]:
        print(f"🎨 Verarbeite Bild: {filename}")
        with Image.open(input_path) as img:
            img.thumbnail(max_size)
            img.convert("RGB").save(final_jpg_path, "JPEG", quality=85)

print("✅ Alle Bilder fertig konvertiert!")
