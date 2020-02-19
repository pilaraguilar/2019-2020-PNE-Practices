from Seq0 import *
folder= "../session-04/"
e = ".txt"
gene = ["U5"]
bases = ['A', 'C', 'T', 'G']

print("Gene U5: ")

seq= seq_read_fasta(folder + gene + e)
comp= seq_complement(seq)
print("Frag: ", {seq})
print("Comp: ", {comp})
