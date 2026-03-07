from pathlib import Path
import shutil
import json
import re
import unicodedata

# ===== INDSTILLINGER =====
GITHUB_USERNAME = "luka2945"
REPO_NAME = "Billede"

SOURCE_DIR = Path("input")
OUTPUT_DIR = Path("af")
OUTPUT_JSON = Path("af/urls.json")

# Hvilke filtyper der tælles som billeder
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".svg"}

def slugify_filename(name: str) -> str:
    """
    Gør filnavnet pænt og web-venligt:
    - æ -> ae
    - ø -> oe
    - å -> aa
    - mellemrum -> bindestreg
    - fjerner mærkelige tegn
    """
    replacements = {
        "æ": "ae", "ø": "oe", "å": "aa",
        "Æ": "ae", "Ø": "oe", "Å": "aa",
    }

    for old, new in replacements.items():
        name = name.replace(old, new)

    name = unicodedata.normalize("NFKD", name)
    name = name.encode("ascii", "ignore").decode("ascii")
    name = name.lower()
    name = re.sub(r"[^a-z0-9._-]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-")
    return name

def main():
    if not SOURCE_DIR.exists():
        print(f"Fejl: mappen '{SOURCE_DIR}' findes ikke.")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    url_map = {}
    copied_files = []

    for file in SOURCE_DIR.iterdir():
        if not file.is_file():
            continue

        if file.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        clean_name = slugify_filename(file.stem) + file.suffix.lower()
        destination = OUTPUT_DIR / clean_name

        # Kopiér billedet til /af
        shutil.copy2(file, destination)

        # URL til GitHub Pages
        url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/af/{clean_name}"

        # Nøgle uden filendelse
        key = Path(clean_name).stem
        url_map[key] = url
        copied_files.append((file.name, clean_name, url))

    # Gem samlet JSON-fil
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(url_map, f, ensure_ascii=False, indent=2)

    # Gem også en txt-oversigt, hvis du vil læse den hurtigt
    txt_path = OUTPUT_DIR / "urls.txt"
    with open(txt_path, "w", encoding="utf-8") as f:
        for _, clean_name, url in copied_files:
            f.write(f"{clean_name} = {url}\n")

    print("Færdig.")
    print(f"Kopierede billeder: {len(copied_files)}")
    print(f"JSON gemt i: {OUTPUT_JSON}")
    print(f"TXT gemt i: {txt_path}")

if __name__ == "__main__":
    main()
