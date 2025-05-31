from pathlib import Path

def write_file(file_name, file_content):
    """Write file_content to a .txt file named file_name.txt"""
    file_path = Path(str(file_name) + ".txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append append_content to a .txt file named file_name.txt"""
    file_path = Path(str(file_name) + ".txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "a") as f:
        f.write(append_content)

def read_file(file_name):
    """Read and return the content of a .txt file named file_name.txt"""
    file_path = Path(str(file_name) + ".txt")
    with open(file_path, "r") as f:
        return f.read()