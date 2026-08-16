from pathlib import Path
import shutil

source = Path("instance/expense_tracker.db")
target = Path("instance/backup.db")
if source.exists():
    shutil.copy2(source, target)
    print("Backup created.")
else:
    print("Database not found.")
