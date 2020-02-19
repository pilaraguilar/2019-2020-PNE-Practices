from Seq0 import *
folder= "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

for g in genes:
    seq= seq_read_fasta2(folder + g + e)
    print("Gene", g, count(seq) )