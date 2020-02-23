from Seq0 import *

FOLDER="../session-04/"
EXT= ".txt"
GENES=["U5", "ADA", "FRAT1", "FXN", "U5"]

print("-----| Exercise 3 |------")

for g in GENES:
    seq=seq_read_fasta2(FOLDER + g + EXT)
    print(f"Gene {g}  lenght: {seq_len(seq)}")