def write_file(file_name, file_content):
    with open(file_name.with_suffix(".txt"), mode = "w", encoding="utf-8") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(file_name.with_suffix(".txt"), mode = "a", encoding="utf-8") as f:
        f.write(append_content)

def read_file(file_name):
    with open(file_name.with_suffix(".txt"), mode = "r", encoding="utf-8") as f:
        return f.read()
