from Seq0 import *
folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']


print("----| Exercise 4 |-----")
for g in genes:
    filename = folder + g + e
    seq = seq_read_fasta(filename)
    print()
    print("Gene", g)
    for b in bases:
        # this loop iterates the function for each base of the list
        print(b, ":", seq_count_base(seq, b))

        
