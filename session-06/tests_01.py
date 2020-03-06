from Seq0 import *

seq1 = "ATTCCCGGGG"
# you have to create a function that help you to know when a sequence is wrong
# -- Check that the sequence is valid


print(f"Seq:    {seq1}")
print(f"  Rev : {seq_reverse(seq1)}")
# the reverse sequence as a parameter
print(f"  Comp: {seq_complement(seq1)}")
print(f"  Length: {seq_len(seq1)}")
print(f"    A: {seq_count_base(seq1, 'A')}")
print(f"    T: {seq_count_base(seq1, 'T')}")
print(f"    C: {seq_count_base(seq1, 'C')}")
print(f"    G: {seq_count_base(seq1, 'G')}")
