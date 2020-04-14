import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078', 'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362',}

GENENAME = input("Write the gene name:")

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + GENES[GENENAME] + PARAMS
print()
print("Server: ", SERVER)
print("URL:", URL)

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + GENES[GENENAME] + PARAMS)

except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# Read the response's body
data1 = r1.read().decode()

# Create a data variable and form the JSON received
gene = json.loads(data1)

termcolor.cprint("Gene: ", 'yellow', end="")
print("MIR633")
termcolor.cprint("Description: ", 'yellow', end="")
print(gene['desc'])
termcolor.cprint("Bases: ", 'yellow', end="")
print(gene['seq'])

gen = gene['seq']
seq = Seq(gen)

sl = s.len
counta = s.seq_count_bases ('A')
porta = "{:.1f}".format(100 * counta / sl)
countc = s.seq_count_bases ('C')
portc = "{:.1f}".format(100 * countc / sl)
countg = s.seq_count_bases('G')
portg = "{:.1f}".format(100 * countg / sl)
countt = s.seq_count_bases ('T')
portt = "{:.1f}".format(100 * countt / sl)

termcolor.cprint("Total lenght: ", "yellow", end="")
print(sl)

