from pathlib import Path
files = [p for p in Path(".").rglob("*") if p.is_file() and ".git" not in p.parts]
print("Project files:", len(files))
for p in sorted(files):
    print(p)
