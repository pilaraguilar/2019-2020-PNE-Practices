from Seq1 import Seq #Seq is the class

print("-----| Practice 1, Exercise 9 |------")
#we are creating a sequence from files in fasta format

FOLDER="../session-04/"
FILENAME= "U5.txt"
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta2(FOLDER + FILENAME)

print("Sequence: ", " (Lenght:", s.len(), ")", s)
print(f"  Bases: {s.count()}")
print("   Rev: ", s.seq_reverse())
print("   Comp: ", s.seq_complement())

