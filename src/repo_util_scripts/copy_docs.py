from pathlib import Path
import shutil

SOURCE_DIR = Path("src/docs")
DEST_DIR = Path("docs")

FILES = [
    "about.md",
    "home.md",
    "assets/vega-scverse-logo.png"
    # Add more filenames here
]

for filename in FILES:
    src = SOURCE_DIR / filename
    dst = DEST_DIR / filename

    dst.parent.mkdir(parents=True, exist_ok=True)

    shutil.copy2(src, dst)
    print(f"Copied '{src}' -> '{dst}'")