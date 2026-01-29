import json
import glob

for file in glob.glob("*.ipynb"):
    with open(file, "r", encoding="utf-8") as f:
        nb = json.load(f)

    nb["metadata"].pop("widgets", None)

    with open(file, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

    print(f"Fixed {file}")
