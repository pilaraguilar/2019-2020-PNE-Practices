from Seq0 import *
folder = "../session-04/"
e = ".txt"
gene = ["U5"]
bases = ['A', 'C', 'T', 'G']


print("-----| Exercise 6 |------")
print("Gene U5: ")
for b in gene:
    seq = seq_read_fasta(folder + b + e)[:20]
    reverse = seq_reverse(seq)
    print("Frag: ", seq)
    print("Rev: ", reverse)

