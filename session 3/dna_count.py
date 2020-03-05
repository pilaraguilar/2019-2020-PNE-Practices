countA = 0
countC = 0
countG = 0
countT = 0

seq_dna = input("Introduce a sequence: ")

for i in seq_dna:
    if i == "A":
        countA += 1
    elif i == "C":
        countC += 1
    elif i == "G":
        countG += 1
    elif i == "T":
        countT += 1


print("Total lenght : ", len(seq_dna))
print("A: ", countA)
print("C: ", countC)
print("G: ", countG)
print("T: ", countT)
