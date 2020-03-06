from pathlib import Path


# -- Constant with the new of the file to open
FILENAME = "RNU6_269.txt"
try:
    # -- Open and read the file
    file_contents = Path(FILENAME).read_text()
    file = file_contents.split("\n")
    # -- Print the head on the console
    print(file[0])

except FileNotFoundError:
    print("File not found")
