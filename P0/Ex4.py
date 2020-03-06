from Seq0 import *
folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 4 |------")
for g in genes:
    seq = seq_read_fasta(folder + g + e)
    print("Gene", g)
    for b in bases:
        # the function seq_count_base give me the count of bases
        print(b, ":", seq_count_base(seq, b))
        
