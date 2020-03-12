from Seq1 import Seq  # Seq is the class

print("-----| Practice 1, Exercise 9 |------")
# we are creating a sequence from files in fasta format

FOLDER = "../Session-04/"
EXT = ".txt"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta(FOLDER + GENES[0] + EXT)

print("Sequence: ", " (Lenght:", s.len(), ")", s)
print("      Bases:", s.count())
print("      Rev: ", s.seq_reverse())
print("      Comp: ", s.seq_complement())
