#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

# === CONFIGURACIÓN ===
INPUT_DIR = Path("./")   # Carpeta de entrada
OUTPUT_DIR = Path("./escalado")  # Carpeta de salida
MAX_SIZE = 256  # Tamaño máximo del lado más largo

# Crear carpeta de salida si no existe
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Extensiones válidas
VALID_EXTENSIONS = [".png", ".jpg", ".jpeg"]

# === PROCESAMIENTO ===
for img_path in INPUT_DIR.glob("*"):
    if img_path.suffix.lower() not in VALID_EXTENSIONS:
        continue

    with Image.open(img_path) as img:
        # Obtener tamaño original
        width, height = img.size

        # Calcular escala
        scale = MAX_SIZE / max(width, height)
        if scale < 1:  # Solo reducimos si excede MAX_SIZE
            new_size = (int(width * scale), int(height * scale))
            resized_img = img.resize(new_size, Image.LANCZOS)
        else:
            resized_img = img.copy()

        # Guardar imagen reescalada
        output_path = OUTPUT_DIR / img_path.name
        resized_img.save(output_path, optimize=True)
        print(f"✅ {img_path.name} -> {output_path.name} ({resized_img.size})")

print("🎨 Reescalado completado.")
