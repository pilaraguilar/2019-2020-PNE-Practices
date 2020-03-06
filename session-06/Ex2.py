# the function print_seqs(seq_list) that receives a list of sequences
# and prints their number in the list, their length and the sequence itself


class Seq:
    def __init__(self, strbases):
        self.strbases = strbases
        # passed as argument when creating the object
        # It is a special method that is called every time a new object is created

    def __str__(self):
        # it run each time something is print
        return self.strbases
        # it gives the internal info of the object

    def len(self):
        # self means inside the method
        return len(self.strbases)


def print_seqs(seq):
    # the function print_seqs(seq_list) that receives a list of sequences
    # and prints their number in the list, their length and the sequence itself
    for s in seq:
        print("Sequence ", seq.index(s), "(Lenght: ", s.len(), ")", s)


seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seqs(seq_list)
