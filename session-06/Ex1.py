class Seq:
    def __init__(self, strbases):#function for initializing the object #strsbases: is a parameter, you can call wherever you want
        self.strbases=strbases # passed as argument when creating the object
        print("New sequence created!") #It is a special method that is called every time a new object is created

        bases=['A', 'C', 'G', 'T']

        for base in strbases:
            if base not in bases:
                print("ERROR!!")
                print("Sequence 2: ERROR!!")
            return


        self.strbases

    def __str__(self): #it run each time something is print
        return self.strbases #it gives the internal info of the object


    def len(self): #self means inside the method
        return len(self.strbases)

s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")
print(f"Sequence 1: {s1}")
