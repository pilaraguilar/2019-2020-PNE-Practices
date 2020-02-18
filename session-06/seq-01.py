class Seq:
    """A class for representing sequence objects"""

    def __init__(self, strbases):#function for initializing the object #strsbases: is a parameter, you can call wherever you want
        self.strbases=strbases
        print("New sequence created!") #cada vez que creas un objeto esto se imprime

    def __str__(self): #it run each time something is print
        return self.strbases #it gives the internal info of the object

    def len(self): #self means inside the method
        return len(self.strbases)

class Gene(Seq):#inherit all the methods of the basesç
    pass
#-- Main project
# #cuando creamos un objeto hay que poner algo dentro

s1= Seq("AACTGC")
#s2= Seq("CTGCATG") #empty object
g=Gene("ACGTACG")

#f means format, is the same that ("hello", variable)
print(f"sequence 2: {g}")
print(f"Sequence 1:  {s1}") #prints the object identification, no the internal info, you have you put the def _str_

l1=s1.len()
print(f"the lenght of the sequence 1 is {l1}")
print(f"the lenght of the sequence 2 is {g.len()}")

print("Testing objects...")
