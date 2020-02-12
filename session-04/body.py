from pathlib import Path

# -- Constant with the new of the file to open
filename = "U5.txt"

# -- Open and read the file
file_contents = Path(filename).read_text()

# -- Print the contents on the console
try:

    with open (filename, "r") as f:
        header=next(f)
        for line in f:
            components = line.replace('\n', "")
            print(components)
        f.close()
except FileNotFoundError:
    print("file not found")
