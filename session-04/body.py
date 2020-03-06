from pathlib import Path


# -- Constant with the new of the file to open
filename = "RNU6_269.txt"
file_contents = Path(filename).read_text()
try:
    with open(filename, "r") as f:
        file = file_contents.split("\n")
        header = next(f)
        for line in f:
            file = line.replace("\n", "")
            print(file)


except FileNotFoundError:
    print("File not found")
