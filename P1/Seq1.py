from pathlib import Path  # for open a file


class Seq:

    def __init__(self, strbases="NULL"):  # function for initializing the object #strsbases: is a parameter, you can
        # call wherever you want
        if strbases == "NULL":
            self.strbases = "NULL"
            print("NULL sequence created")
            self.lenght = 0

        else:
            ok = True
            p = 0  # position in the sequence

            while p < len(strbases) and ok:
                if strbases[p] != "T" and strbases[p] != "C" and strbases[p] != "A" and strbases[p] != "G":
                    self.strbases = "ERROR"
                    self.length = 0
                    ok = False
                    print("INVALID Sequence")

                else:
                    p += 1

            if ok and strbases != "NULL":
                print("New sequence created!")
                self.strbases = strbases
                self.length = len(self.strbases)

    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):
        return len(self.strbases)


    def seq_count_bases(self, b):  # it applies to the dictionary,
        return self.strbases.count(b)

    def count(self):  # times that a base is repited
        e = {"A": self.seq_count_bases("A"), 'T': self.seq_count_bases('T'),
             'C': self.seq_count_bases('C'), 'G': self.seq_count_bases('G')}

        return e

    def seq_reverse(self):
        if self.strbases != "NULL" and self.strbases!= "ERROR":
            return self.strbases[::-1]
        elif self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"

    def seq_complement(self):
        e = {"A": "T", 'T': 'A', 'C': 'G', 'G': 'C'}
        es = ""
        if self.strbases != "NULL" and self.strbases!= "ERROR":
            for b in self.strbases:
                es += e[b]
        elif self.strbases == "NULL":
            return "NULL"
        elif self.strbases == "ERROR":
            return "ERROR"

        return es

    def seq_read_fasta(self, filename):
        #  read the text
        content = Path(filename).read_text()
        # Remove the head
        body = content.split('\n')[1:]
        # Store the sequence
        self.strbases = "".join(body)

        return self
    def seq_count_base(self, param):
        pass
