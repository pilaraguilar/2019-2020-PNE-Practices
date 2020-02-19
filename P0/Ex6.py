from Seq0 import *
folder= "../session-04/"
e = ".txt"
gene = ["U5"]
bases = ['A', 'C', 'T', 'G']

print("Gene U5: ")
for g in gene:
    seq=seq_read_fasta(folder + g + e)
    reverse= seq_reverse(seq)
    print("Frag: ", seq)
    print("Rev: ", reverse)

