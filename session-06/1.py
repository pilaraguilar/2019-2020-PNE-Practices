class Seq:
    # function for initializing the object #strsbases: is a parameter, you can call wherever you want
    def __init__(self, strbases):
        self.strbases = strbases
        # passed as argument when creating the object
        print("New sequence created!")
        # It is a special method that is called every time a new object is created

    # it run, each time something is print
    def __str__(self):
        return self.strbases
        # it gives the internal info of the object

    # self means inside the method
    def len(self):
        return len(self.strbases)


s1 = Seq("ACCTGC")
s2 = Seq("Hello? Am I a valid sequence?")


print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")


# As the Gene is also a Seq, for creating a Gene first we should call the init function from the Seq class.
# We do it by calling the super().init(strbases) method.
# And then we add the properties of the Gene. In this case its name
# all the Genes are sequences
