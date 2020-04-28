from Seq0 import *
folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']


print("----| Exercise 5 |-----")
for g in genes:
    filename = folder + g + e
    seq = seq_read_fasta(filename)
    # the function count returns a dictionary with the number of times of each base
    print("Gene", g, seq_count(seq))
