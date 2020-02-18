class Seq:
    def __init__(self, strbases):#function for initializing the object #strsbases: is a parameter, you can call wherever you want
        self.strbases=strbases
        print("New sequence created!") #cada vez que creas un objeto esto se imprime

    def __str__(self): #it run each time something is print
        return self.strbases #it gives the internal info of the object

    def len(self): #self means inside the method
        return len(self.strbases)

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")

for i in s2:
    if i!= "A" and i!="C" and i!="T" and i!="G":
        print("Sequence 2: Error")


