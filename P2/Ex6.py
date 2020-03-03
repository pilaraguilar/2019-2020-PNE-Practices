from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")


IP = "192.168.1.43"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"

#Create a client object
c = Client(IP, PORT)

#Print the IP and PORTs
print(c)

#Read the Gene from a file
s = Seq().read_fasta2(FOLDER + GENE + EXT)

#get the string

bases= srt(s)

lenght=10
c.talk("sending", {gene}, "gene to the server, in fragments of ", {lenght}, "bases...")

for i in range(5):
    fragment= bases[i *10: (i + 1)*10]

    #Print on Client's console
    print(f"Fragment {i + 1}: {frag}")

    #Send the fragment to the server!
    c.talk(f"Fragment {i + 1}: {frag}")

