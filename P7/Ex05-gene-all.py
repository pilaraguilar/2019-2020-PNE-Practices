import http.client
import json
import termcolor
from Seq1 import Seq

GENES = {'FRAT1': 'ENSG00000165879', 'ADA': 'ENSG00000196839', 'FXN': 'ENSG00000165060',
         'RNU6_269P.txt': 'ENSG00000212379',
         'MIR633': 'ENSG00000207552', 'TTTY4C': 'ENSG00000228296', 'RBMY2YP': 'ENSG00000227633',
         'FGFR3': 'ENSG00000068078', 'KDR': 'ENSG00000128052', 'ANK2': 'ENSG00000145362', }

for gene in GENES:
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id/'
    PARAMS = '?content-type=application/json'
    URL = SERVER + ENDPOINT + GENES[gene] + PARAMS
    print()
    print("Server: ", SERVER)
    print("URL:", URL)

    # Connect with the server
    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + GENES[gene] + PARAMS)

    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    # response message from the server
    r1 = conn.getresponse()

    # status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

    # Read the response's body
    data1 = r1.read().decode()

    # Create a data variable and form the JSON received
    gen = json.loads(data1)

    termcolor.cprint("Gene: ", 'yellow', end="")
    print(gene)
    termcolor.cprint("Description: ", 'yellow', end="")
    print(gen['desc'])
    termcolor.cprint("Bases: ", 'yellow', end="")
    print(gen['seq'])

    ge = gen['seq']
    s = Seq(ge)

    sl = s.len()
    counta = s.seq_count_bases('A')
    porta = round((100 * counta / sl), 2)
    countc = s.seq_count_bases('C')
    portc = round((100 * countc / sl), 2)
    countg = s.seq_count_bases('G')
    portg = round((100 * countg / sl), 2)
    countt = s.seq_count_bases('T')
    portt = round((100 * countt / sl), 2)

    termcolor.cprint("Total lenght: ", "yellow", end="")
    print(sl)
    termcolor.cprint("A: ", "blue", end="")
    print(counta, ",", porta, "%")
    termcolor.cprint("C: ", "blue", end="")
    print(countc, ",", portc, "%")
    termcolor.cprint("T: ", "blue", end="")
    print(countt, ",", portt, "%")
    termcolor.cprint("G: ", "blue", end="")
    print(countg, ",", portg, "%")
    BASES = ["A", "C", "G", "T"]

    if counta > countt and counta > countt and counta > countg:
        termcolor.cprint("Most frequent base: ", "yellow", end="")
        print("A")

    elif countc > countt and countc > counta and countc > countg:
        termcolor.cprint("Most frequent base: ", "yellow", end="")
        print("C")

    elif countg > countt and countg > counta and countg > countc:
        termcolor.cprint("Most frequent base: ", "yellow", end="")
        print("G")

    else:
        termcolor.cprint("Most frequent base: ", "yellow", end="")
        print("T")
    valid = True
