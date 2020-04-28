from Seq0 import *

folder = "../session-04/"
e = ".txt"
genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269"]
bases = ['A', 'C', 'T', 'G']

print("----| Exercise 8 |------")


for g in genes:
    seq = seq_read_fasta(folder + g + e)
    dictionary = seq_count(seq)
    min_value = 0
    max_value = 9999999999999999999999999999999999999999999999999999
    #we fix a maximum and a minimum

    for b, v in dictionary.items():
        while v > min_value:
            min_value = v
            max_value = b

            # repeat that loop until we find the maximum

    print( "Gene", g, "Most frequent base:", max_value)
