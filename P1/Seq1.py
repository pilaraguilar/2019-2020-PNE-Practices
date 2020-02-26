from pathlib import Path #for open a file

class Seq:
    NULL="NULL"
    ERROR="ERROR"

    def __init__(self, strbases= NULL):  # function for initializing the object #strsbases: is a parameter, you can call wherever you want
        if strbases== self.NULL:
            self.strbases=self.NULL
            print("NULL sequence created")
            return

        if not self.valid_str(strbases):
            self.strbases = self.ERROR #you have always have to put self to operate with an object
            print("INVALID Seq!")
            return

        #string in the object
        self.strbases = strbases
        print("New sequence created!")

        

    def __str__(self):  # it run each time something is print
        return self.strbases  # it gives the internal info of the object

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0 #a 0 if it is null or invalid
        else:
            return len(self.strbases)

    def seq_read_fasta(filename): #Open a DNA file in FASTA format and return the sequence as a string
        file_contents= Path(filename).read_text() #read the file
        seq_dna=file_contents
        index_finish= seq_dna.find("\n")
        seq_dna= seq_dna[index_finish +1:]
        seq_dna=seq_dna.replace("\n", "")
        seq_dna=seq_dna[:20]
        return seq_dna

    def valid_str(self, strbases):    #self argument is always the first
        valid_b=["A", "C", "G", "T"]
        for b in strbases :
            if b not in valid_b: #if there is any invalid base
                return False
        return True #valid



    def seq_read_fasta2(self, filename):
        c= Path(filename).read_text() #reading the file
        b=c.split("\n")[1:] #deleting the head
        self.strbases = "".join(b)  #storing the sequence
        return self.strbases




    def seq_count_bases(self, b): #it applies to the dictionary,
        return self.strbases.count(b)


    def count(self):  #times that a base is repited
        e={"A": self.seq_count_bases( "A"), 'T': self.seq_count_bases('T'),
               'C': self.seq_count_bases( 'C'), 'G': self.seq_count_bases( 'G')}

        return e



    def seq_reverse(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0  #a 0 if it is null or invalid
        else:
            return self.strbases[::-1]

    def seq_complement(self):
        e = {"A": "T", 'T':'A', 'C':'G', 'G' :'C'}
        es=""
        if self.strbases in [self.NULL, self.ERROR]:
            return self.strbases

        for b in self.strbases:
            es += e[b]

        return es




