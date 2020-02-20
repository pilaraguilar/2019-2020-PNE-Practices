import termcolor

class Seq:
    def __init__(self, strbases):  # function for initializing the object #strsbases: is a parameter, you can call wherever you want
        self.strbases = strbases  # passed as argument when creating the object
        print("New sequence created!")
    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):  # self means inside the method
        return len(self.strbases)


def print_seqs(seq, color):
    # the function print_seqs(seq_list) that receives a list of sequences and prints their number in the list, their length and the sequence itself
    for s in seq:
        termcolor.cprint(f"Sequence {seq.index(s)}: (Length: {s.len()}) {s}", color)
def generate_seqs(seq, number):
    seqs=[]
    for  letter in range( 1,number+ 1):
        seqs.append(Seq(seq * letter))
    return seqs

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1", 'blue')
print_seqs(seq_list1, "blue")
print()
termcolor.cprint("List 2:", 'green')
print_seqs(seq_list2, 'green')