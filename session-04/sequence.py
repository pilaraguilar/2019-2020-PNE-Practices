from pathlib import Path

# -- Constant with the new of the file to open


# -- Open and read the file

counter=0
# -- Print the contents on the console
try:
    filename = "ADA.txt"
    file_contents = Path(filename).read_text()
    content=file_contents.split("\n")[1:]
    body= ",".join(content).replace(",", "")
    print("body of U5.txt file: ")
    print(len(body))

except FileNotFoundError:
    print("File not found")
