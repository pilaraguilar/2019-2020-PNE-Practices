from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "U5"

# Create a client object
c = Client(IP, PORT)

# Print the IP and PORTs
print(c)

# Read the Gene from a file
s = Seq().seq_read_fasta(FOLDER + GENE + EXT)

# Sending
c.debug_talk(f"Sending {GENE} Gene to the server...")
c.debug_talk(str(s))
