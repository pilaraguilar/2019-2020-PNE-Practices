from pathlib import Path


try:
    filename = "ADA.txt"
    file_contents = Path(filename).read_text()
    content=file_contents.split("\n")[1:]
    body= ",".join(content).replace(",", "")
    print("Body of U5.txt file: ")
    print(len(body))

except FileNotFoundError:
    print("File not found")


