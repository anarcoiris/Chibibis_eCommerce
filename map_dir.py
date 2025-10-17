#!/usr/bin/env python3
"""
map_dir.py — Mapea la estructura de archivos de un directorio,
excluyendo .venv/, .git/ y __pycache__.
"""

from pathlib import Path

EXCLUDE_DIRS = {".venv", ".git", "__pycache__"}

def map_directory(root: Path, prefix: str = "") -> None:
    """Imprime la estructura de archivos desde el directorio root."""
    entries = sorted(
        [p for p in root.iterdir() if not (p.name in EXCLUDE_DIRS or p.name.startswith('.'))],
        key=lambda p: (p.is_file(), p.name.lower())
    )
    
    for i, entry in enumerate(entries):
        connector = "└── " if i == len(entries) - 1 else "├── "
        print(prefix + connector + entry.name)
        if entry.is_dir():
            extension = "    " if i == len(entries) - 1 else "│   "
            map_directory(entry, prefix + extension)

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Mapea la estructura de un directorio.")
    parser.add_argument(
        "directory", nargs="?", default=".", help="Ruta del directorio raíz (por defecto: actual)"
    )
    args = parser.parse_args()

    root = Path(args.directory).resolve()
    print(f"{root.name}/")
    map_directory(root)

if __name__ == "__main__":
    main()
