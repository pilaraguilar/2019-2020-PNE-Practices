from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.43"
PORT1 = 8080
PORT2=8081

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"


c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)

#Print the IP and PORTs
print(c1)
print(c2)

#Read the Gene from a file
s = Seq().read_fasta2(FOLDER + GENE + EXT)


bases = str(s)

#Print the Gene
print(f"Gene {GENE}: {bases}")


LENGTH = 10

#initial message to both servers
initial_msg = f"Sending {GENE} Gene to the server, in fragments of {LENGTH} bases..."

c1.talk(initial_msg)
c2.talk(initial_msg)

#Create the framents
#sending them to the servers
for i in range(10):

    frag = bases[i*LENGTH:(i+1)*LENGTH]

    #Print on Client's console
    print(f"Fragment {i+1}: {frag}")

    #Message to send to the server
    msg = f"Fragment {i+1}: {frag}"

    #even fragments (counting from 0) are sent to server 1
    if i % 2:
        c2.talk(msg)

    #Odd segments are sent to server 2
    else:
        c1.talk(msg)