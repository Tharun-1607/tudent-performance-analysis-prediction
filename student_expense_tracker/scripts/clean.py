from pathlib import Path

for path in Path(".").rglob("*.pyc"):
    path.unlink(missing_ok=True)
print("Python cache files cleaned.")
