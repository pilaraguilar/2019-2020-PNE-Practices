from Seq1 import Seq
print("-----| Practice 1, Exercise 4 |------")

#null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")



print("Sequence 1: (Lenght:", s1.len(), ")", s1)
print("Sequence 2: (Lenght:", s2.len(), ")", s2)
print("Sequence 3: (Lenght:", s3.len(), ")", s3)