from Seq0 import *

folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 8 |------")

for g in genes:
    seq = seq_read_fasta(folder + g + e)
    # we return the dictionary created in count function
    dictionary = count(seq)
    # then we, write it in a list
    lit = list(dictionary.values())
    # calculating the most common base
    most_common = max(lit)
    print("Gene ", g, ": Most frequent Base:", bases[lit.index(most_common)])
