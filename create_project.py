from pathlib import Path

root = Path(".")

# All folders list

folders = [
    "app/api",
    "app/core",
    "app/rag",
    "app/services",
    "data",
    "templates",
    "static",
    "uploads",
    "tests"
]

# All file lists

files = [
    "app/main.py",
    "ingest_sample_kb.py",
    "requirements.txt",
    ".env",
    "run.py"
]

for folder in folders:
    (root/folder).mkdir(parents=True,exist_ok=True)

for file in files:
    (root/file).touch(exist_ok=True)