# in this exercise we program a client for connecting
# to the sequence endpoint and we get the sequence and it description

import http.client
import json
import termcolor


GENES = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060', 'RNU6_269P.txt': 'ENSG00000212379', 'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633', 'FGFR3': 'ENSG00000068078', 'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362',}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + GENES["MIR633"] + PARAMS
print()
print("Server: ", SERVER)
print("URL:", URL)

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", ENDPOINT + GENES["MIR633"] + PARAMS)

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
