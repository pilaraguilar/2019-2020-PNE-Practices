from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6

print("-----| Practice ", PRACTICE, "Exercise", EXERCISE, "|------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session-04/"
EXT = ".txt"
GENE = "FRAT1"
filename = FOLDER + GENE + EXT

# Create a client object
c = Client(IP, PORT)

# Print the IP and PORTs
print(c)

# Read the Gene from a file
s = Seq().seq_read_fasta(filename)


# get the string
bases = str(s)

lenght = 10
c.talk(f"Sending {GENE} Gene to the server, in fragments of {lenght} bases...")

for i in range(5):
    # de 10 en 10
    fragment = bases[i * 10: (i + 1) * 10]

    # Print on Client's console
    print(f"Fragment {i + 1}: {fragment}")

    # Send the fragment to the server
    c.talk(f"Fragment {i + 1}: {fragment}")
