from Seq1 import Seq  # Seq is the class

print("-----| Practice 1, Exercise 8 |------")
# we are creating sequences passing a string with the bases to an object

# null sequence
s1 = Seq()

# valid sequence
s2 = Seq("ACTGA")

# invalid sequence
s3 = Seq("Invalid sequence")

for i, s in enumerate([s1, s2, s3]):
    print("Sequence", i, ": (Lenght:", s.len(), ")", s)
    print("  Bases:", s.count())
    print("   Rev: ", s.seq_reverse())
    print("   Comp: ", s.seq_complement())
