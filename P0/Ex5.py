from Seq0 import *
folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 5 |------")
for g in genes:
    seq = seq_read_fasta(folder + g + e)
    # the function count returns a dictionary with the number of times of each base
    print("Gene", g, count(seq))
