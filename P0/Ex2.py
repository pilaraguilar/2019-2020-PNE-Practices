from Seq0 import *

folder = "../session-04/"
filename = "U5.txt"

file = folder + filename

print("Exercise 2")
print("DNA file: ", filename)
print("The first 20 bases are: ", seq_read_fasta(file)[:20])
