from pathlib import Path
import shutil

SOURCE_DIR = Path("src/docs")
DEST_DIR = Path("docs")

FILES = [
    "about.md",
    "home.md",
    # Add more filenames here
]

for filename in FILES:
    src = SOURCE_DIR / filename
    dst = DEST_DIR / filename

    dst.parent.mkdir(parents=True, exist_ok=True)

    if not dst.exists():
        shutil.copy2(src, dst)
        print(f"Copied '{src}' -> '{dst}'")
    else:
        print(f"'{dst}' already exists. Skipping.")