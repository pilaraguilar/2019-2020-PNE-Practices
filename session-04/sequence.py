from pathlib import Path


try:
    filename = "ADA.txt"
    file_contents = Path(filename).read_text()
    content = file_contents.split("\n")

    # REMOVE THE HEAD
    content = file_contents[1:]

    # JOINING ALL THE ELEMENTS REMOVING THE COMMAS
    body = ",".join(content).replace(",", "")
    print("Body of ADA.txt file: ")
    print(len(body))

except FileNotFoundError:
    print("File not found")
