from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

folder= "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

s = Seq()

for g in genes:
    se= s.seq_read_fasta2(folder + g + e)
    d= se.count(se)
    lit=list(d.values())
    most_common= max(lit)
    print("Gene ", {g}, ": Most frequent Base:", {bases[lit.index(most_common)]})