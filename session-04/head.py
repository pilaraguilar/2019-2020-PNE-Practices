from pathlib import Path

# -- Constant with the new of the file to open
filename = "RNU6_269.txt"

# -- Open and read the file
file_contents = Path(filename).read_text()

# -- Print the contents on the console
try:

    with open (filename, "r") as f:
        header=next(f)
        print(header)
except FileNotFoundError:
    print("file not found")