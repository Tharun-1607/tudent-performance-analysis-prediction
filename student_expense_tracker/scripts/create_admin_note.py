from pathlib import Path
Path("ADMIN_NOTE.txt").write_text(
    "This project currently has no authentication. Add authentication before production use.",
    encoding="utf-8"
)
print("Created ADMIN_NOTE.txt")
