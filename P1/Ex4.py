from Seq1 import Seq
print("-----| Practice 1, Exercise 4 |------")
#we are creating sequences passing a string with the bases to an object

#null sequence
s1 = Seq()

# valid sequence
s2 = Seq("ACTGA")

# invalid sequence
s3 = Seq("Invalid sequence")



print("Sequence 1: (Lenght:", s1.len(), ")", s1)
print("Sequence 2: (Lenght:", s2.len(), ")", s2)
print("Sequence 3: (Lenght:", s3.len(), ")", s3)