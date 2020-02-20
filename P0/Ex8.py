from Seq0 import *

folder= "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 8 |------")

for g in genes:
    seq= seq_read( folder + g + e)
    dictionary= count(seq)
    lit= list(dictionary.values())
    most_common= max(lit)
    print("Gene ", {g}, ": Most frequent Base:", {bases[lit.index(most_common)]})