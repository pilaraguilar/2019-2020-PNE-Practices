from pathlib import Path

file = Path("dna.txt")

print("File: ", file)

info = file.read_text()

print("Info: ", info)

A = 0
G = 0
C = 0
T = 0
idk = 0

for base in info:
    if base == "A":
        A += 1
    elif base == "C":
        C += 1
    elif base == "G":
        G += 1
    elif base == "T":
        T += 1
    else:
        idk += 1

print("Total length: ", len(info))
print("A: ", A)
print("C: ", C)
print("G: ", G)
print("T: ", T)

print("unknows: ", idk)

