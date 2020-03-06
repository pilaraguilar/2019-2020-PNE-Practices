class Seq:
    """A class for representing sequence objects"""

    # function for initializing the object
    # strsbases: is a parameter, you can call wherever you want
    # called every time a new object is created
    # cada vez que creas un objeto esto se imprime
    # strbases is an attribute
    def __init__(self, strbases):
        self.strbases = strbases
        # to store the info in the attirbute of the object we put self
        print("New sequence created!")

    # it run each time something is print
    # it gives the internal info of the object
    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

# inherit all the methods of the bases


class Gene(Seq):
    pass


# -- Main project
# cuando creamos un objeto hay que poner algo dentro

s1 = Seq("AACTGC")
# s2 = Seq() # empty object
g = Gene("ACGTACG")

# f means format, is the same that ("hello", variable)
print(f"sequence 2: {g}")
print(f"Sequence 1:  {s1}")
# prints the object identification, no the internal info, you have you put the def _str_

l1 = s1.len()
print(f"the lenght of the sequence 1 is {l1}")
print(f"the lenght of the sequence 2 is {g.len()}")

print("Testing objects...")

g = Gene("CAGTAC")
print(f"Gene: {g}")
