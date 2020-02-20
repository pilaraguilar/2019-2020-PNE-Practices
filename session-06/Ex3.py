#The function generate_seqs(pattern, number)
#It will create a list with the given number of sequences
#This pattern is a string of one or more bases.
 #The first sequence of the list will have only the pattern. In the second, the pattern is repeated twice.


class Seq:
    def __init__(self, strbases):  # function for initializing the object #strsbases: is a parameter, you can call wherever you want
        self.strbases = strbases  # passed as argument when creating the object
        print("New sequence created!")
    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):  # self means inside the method
        return len(self.strbases)


def print_seqs(seq):
    # the function print_seqs(seq_list) that receives a list of sequences and prints their number in the list, their length and the sequence itself
    for s in seq:
        print(f"Sequence {seq.index(s)}: (Length: {s.len()}) {s}")
def generate_seqs(seq, number):
    seqs=[]
    for  letter in range( 1,number+ 1):
        seqs.append(Seq(seq * letter))
    return seqs

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)