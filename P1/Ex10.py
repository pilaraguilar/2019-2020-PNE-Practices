from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")

folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

for g in genes:
    se = Seq().seq_read_fasta(folder + g + e)
    d = se.count()
    lit = list(d.values())  # creating a list with the value at the dictionary
    most_common = max(lit)  # calculating the "maximun" that is the base that repited more times
    print("Gene ", g, ": Most frequent Base:", bases[lit.index(most_common)])
