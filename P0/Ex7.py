from Seq0 import *
folder= "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "U5"]
bases = ['A', 'C', 'T', 'G']

print("-----| Exercise 7 |------")
print("Gene U5: ")

seq= seq_read(folder + genes[0] + e)
comp= seq_complement(seq)
print("Frag: ", {seq})
print("Comp: ", {comp})
