import http.server
import socketserver
from Seq1 import Seq

import requests

PORT = 8080

SERVER = 'http://rest.ensembl.org'
ENDPOINTS = ["/listSpecies", "/karyotype", "/chromosomeLenght", "/geneSeq", "/geneInfo", "/geneCalc", "/geneList"]
ext = ['/info/species?', '/info/assembly/', "/xrefs/symbol/homo_sapiens/", '/sequence/id/', "/overlap/region/human/"]

# This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")
        request_line = self.requestline
        command = self.command
        path = self.path
        contents = ""

        print("Request line:", request_line)
        print("  Command: ", command)
        print("  Path: ", path)

        # Main page
        if path == "/" or path == "/index.html":
            # The main page will be shown
            with open("index.html", 'r') as f:
                contents = f.read()

        elif path != "/" and path != "index.html":
            # Cut the path to get the endpoints and its options
            option = path.split('?')

            # -------- BASIC LEVEL ------------------------------------------------------------------
            # ----------------------List of Species -------------------------------------------------
            if option[0] == ENDPOINTS[0]:
                conn = requests.get(SERVER + ext[0], headers={"Content-Type": "application/json"})
                data = conn.json()

                # We choose the right part of the ? in the path and then cut into two parts to get the limit
                limit = option[1].split("=")[1]
                print("Limit: ", limit)

                if limit != "":
                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Species List</title>
                                   </head>
                                   <body style="background-color: #F6D8FF;">
                                   <h1><b><FONT face = "Courier New">List of species</FONT></b></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p>The total number of species in the ensembl is: 286 <p>
                                   <p>You have selected the limit: {} <p>
                                   <p>The names of the species are: <P>
                                   <ol> {} </ol>
                                   </body>
                                   </html>"""

                    species_list = ""
                    # this is a loop that stops at the limit
                    for i in range(len(data['species'][:int(limit)])):
                        species_list = species_list + "<li>"
                        species_list = species_list + data['species'][i]['common_name']
                        species_list = species_list + "</li>"
                    species_list = species_list + "</ol></body></html>"

                    # add the information into the html page
                    contents = contents.format(limit, species_list)

                # if you push the send button without put any limit
                elif limit == "":
                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Species List</title>
                                   </head>
                                   <body style="background-color: #F6D8FF;">
                                   <h1><b><FONT face = "Courier New">List of species</FONT></b></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p>The total number of species in the ensembl is: 286 <p>
                                   <p>You have not selected a limit <p>
                                   <p>The names of the species are: <P>
                                   <ol> {} </ol>
                                   </body>
                                   </html>"""

                    species_list = ""
                    for i in range(len(data['species'])):
                        species_list = species_list + "<li>"
                        species_list = species_list + data['species'][i]['common_name']
                        species_list = species_list + "</li>"
                    species_list = species_list + "</ol></body></html>"
                    contents = contents.format(species_list)

            # ------------------- Karyotype ------------------------------------------------------

            elif option[0] == ENDPOINTS[1]:
                try:
                    # to get from the path the chosen specie
                    sp = option[1].split("=")
                    specie = sp[1]

                    print("The specie to study is: ", specie)

                    conn = requests.get(SERVER + ext[1] + specie, headers={"Content-Type": "application/json"})
                    data = conn.json()

                    contents = """<!DOCTYPE html> 
                                   <html lang="en"> 
                                   <head>
                                        <meta charset="UTF-8">
                                        <title>Karyotype</title>
                                   </head>
                                   <body style="background-color: #F6D8FF;">
                                   <h1><b><FONT face = "Courier New">Karyotype</FONT></b></h1>
                                   <a href="/"> Main page </a>
                                   <hr>
                                   <p> Names of the chromosomes of the: {} <P>
                                   <ol> {} </ol>
                                   
                                   </body>
                                   </html>"""
                    # we create a list with the karyotype of the data from the ensembl
                    karyotype_list = list(data['karyotype'])

                    # sometimes the ensembl does not have the karyotype of a species
                    # if the list is not empty, the ensembl has it
                    if karyotype_list != list():
                        k_list = ""
                        for cro in karyotype_list:
                            # the chromosome MT is not valid
                            if cro == "MT":
                                pass

                            # add each chromosome in the list
                            elif cro != "MT":
                                k_list = k_list + "<li type=square>"
                                k_list = k_list + cro
                                k_list = k_list + "</li>"
                        # add the lkist of chromosomes to our html page
                        contents = contents.format(specie, k_list)

                    # if the ensembl does not have the karyotype about a specie
                    elif karyotype_list == list():
                        k_list = "Sorry, we don't have information about the karyotype of this specie"
                        contents = contents.format(specie, k_list)

                # when the specie is not valid or we press the send button without filling the box
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Error</title>
                                       </head>
                                       <body style="background-color: #FE2E2E;">
                                       <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr>
                                       <p> Sorry this specie is not valid </p>
                                       </body>
                                       </html>"""

            # ----------------------- Chromosome lenght ---------------------------------------------------

            elif option[0] == ENDPOINTS[2]:
                try:
                    # separate the chromsome and the specie from the path
                    sp = option[1]
                    spe = sp.split("&")[0]
                    c = sp.split("&")[1]
                    specie = spe.split("=")[1]
                    chromo = c.split("=")[1]

                    conn = requests.get(SERVER + ext[1] + specie, headers={"Content-Type": "application/json"})
                    data = conn.json()

                    lenght = None
                    try:
                        for i in data['top_level_region']:
                            if i['coord_system'] == 'chromosome' and i['name'] == chromo:
                                lenght = i['length']

                        if lenght != None:
                            contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Lenght</title>
                                           </head>
                                           <body style="background-color: #F6D8FF;">
                                           <h1><b><FONT face = "Courier New">Chromosome lenght</FONT></b></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Selected specie: {}</p>
                                           <p> Selected chromosome: {}</p>
                                           <p> Lenght of the chromosome: {} <P>
                                           </body>
                                           </html>"""
                            # add to the html page
                            contents = contents.format(specie, chromo, lenght)

                        # if the chromosome is not valid
                        else:
                            contents = """<!DOCTYPE html> 
                                               <html lang="en"> 
                                               <head>
                                                    <meta charset="UTF-8">
                                                    <title>Error</title>
                                               </head>
                                               <body style="background-color: #FE2E2E;">
                                               <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                               <a href="/"> Main page </a>
                                               <hr>
                                               <p> Sorry, this chromosome is not valid for the specie you choose</p>
                                               </body>
                                               </html>"""

                    except IndexError:
                        contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please enter a valid specie and chromosome </p>
                                           </body>
                                           </html>"""
                # if the boxes are in white
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                               <html lang="en"> 
                                               <head>
                                                    <meta charset="UTF-8">
                                                    <title>Error</title>
                                               </head>
                                               <body style="background-color: #FE2E2E;">
                                               <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                               <a href="/"> Main page </a>
                                               <hr>
                                               <p> Please enter a valid specie and chromosome</p>
                                               </body>
                                               </html>"""

            # ------- MEDIUM LEVEL -----------------
            # -------------- Gene seq ---------------------------------------

            elif option[0] == ENDPOINTS[3]:
                # separate the gene from the path
                gene = option[1].split("=")[1]
                try:
                    # connectiog to the fisrt endpoint
                    conn1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = conn1.json()
                    # taking the id from the gene
                    i = data1[0]
                    id = i["id"]
                    # with the id of the gene we connect to the second endpoint
                    conn2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = conn2.json()
                    # taking the sequence
                    seq = data2["seq"]

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: #F6D8FF;">
                                       <h1><b><FONT face = "Courier New">Gene sequence</FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p> Sequence: </p>
                                       <textarea readonly rows="60" cols="75" 
                                       style="background-color:#F6D8FF"> {} </textarea>
                                       
                                       </body>
                                       </html>"""
                    # add to the contents
                    contents = contents.format(gene, seq)

                # in case that the gene is not valid
                except IndexError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please write a valid human gene </p>
                                           </body>
                                           </html>"""
                # in case that you dont fill the box
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please fill the box </p>
                                           </body>
                                           </html>"""

            # -------------- Gene Info --------------------------------

            elif option[0] == ENDPOINTS[4]:
                self.send_response(200)
                # get the gene from the path
                gene = option[1].split("=")[1]
                try:
                    # connecting to the ensembl with that gene
                    conn1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = conn1.json()
                    # get the id
                    i = data1[0]
                    id = i["id"]
                    # connect to the second endpoint with the id
                    conn2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = conn2.json()
                    # get the sequence
                    seq = data2["seq"]
                    c = data2["desc"]
                    h = c.split("chromosome:")
                    # separate the start from the end and from the chromosome
                    n = h[1].split(":")
                    start = n[2]
                    end = n[3]
                    ch = n[1]
                    lenght = len(seq)
                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Info</title>
                                       </head>
                                       <body style="background-color: #F6D8FF;">
                                       <h1><b><FONT face = "Courier New">Information about the gene </FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p><b>Information: </b></p>
                                       <P> Id: {} </p>
                                       <p> Lenght: {}</p>
                                       <p> End: {}</p>
                                       <p> Start: {}</p>
                                       <p> Chromosome: {}</p>
                                       </body>
                                       </html>"""
                    # add our data to the html file
                    contents = contents.format(gene, id, lenght, end, start, ch)

                # when the gene is not valid
                except IndexError:
                    contents = """<!DOCTYPE html> 
                          <html lang="en"> 
                          <head>
                               <meta charset="UTF-8">
                               <title>Error</title>
                          </head>
                          <body style="background-color: #FE2E2E;">
                          <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                          <a href="/"> Main page </a>
                          <hr>
                          <p> Please write a valid human gene </p>
                          </body>
                          </html>"""

                # in case that you do not fill the box
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                           <html lang="en"> 
                                           <head>
                                                <meta charset="UTF-8">
                                                <title>Error</title>
                                           </head>
                                           <body style="background-color: #FE2E2E;">
                                           <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                           <a href="/"> Main page </a>
                                           <hr>
                                           <p> Please fill the box </p>
                                           </body>
                                           </html>"""

            # ------------ Gene Calculations ---------------
            elif option[0] == ENDPOINTS[5]:
                self.send_response(200)
                # get the gene from the path
                gene = option[1].split("=")[1]
                try:
                    # connect to the endpoint to get the id of th gene
                    conn1 = requests.get(SERVER + ext[2] + gene, headers={"Content-Type": "application/json"})
                    data1 = conn1.json()
                    i = data1[0]
                    id = i["id"]
                    # connect to sequence/id endpoint to get the sequence of the gene with the id obtained
                    conn2 = requests.get(SERVER + ext[3] + id, headers={"Content-Type": "application/json"})
                    data2 = conn2.json()
                    # get the sequence
                    sequence = data2["seq"]
                    # import the class
                    seq = Seq(sequence)

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: #F6D8FF;">
                                       <h1><b><FONT face = "Courier New">Calculations</FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p> Selected gene:  {} <P>
                                       <p> The lenght of the sequence is: {} </P>
                                       <p>The percentage of A is: {} %</p>
                                       <p>The percentage of G is: {} %</p>
                                       <p>The percentage of C is: {} %</p>
                                       <p>The percentage of T is: {} %</p>
                                       
                                       </body>
                                       </html>"""
                    # calculate the percentages
                    porta = round(seq.seq_count_bases("A") / len(sequence), 2)
                    portg = round(seq.seq_count_bases("G") / len(sequence), 2)
                    portc = round(seq.seq_count_bases("C") / len(sequence), 2)
                    portt = round(seq.seq_count_bases("T") / len(sequence), 2)

                    contents = contents.format(gene, len(sequence), porta, portg, portc, portt)

                # if the gene does not exist
                except IndexError:
                    contents = """<!DOCTYPE html> 
                          <html lang="en"> 
                          <head>
                               <meta charset="UTF-8">
                               <title>Error</title>
                          </head>
                          <body style="background-color: #FE2E2E;">
                          <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                          <a href="/"> Main page </a>
                          <hr>
                          <p> Please write a valid human gene </p>
                          </body>
                          </html>"""

                    # in case that you dont fill the box
                except KeyError:
                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Error</title>
                                       </head>
                                       <body style="background-color: #FE2E2E;">
                                       <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr>
                                       <p> Please fill the box </p>
                                       </body>
                                       </html>"""

            # ----------- Gene List -------------------------------------
            elif option[0] == ENDPOINTS[6]:
                # separate the chromo, the start and the end
                i = option[1].split("&")
                chromo = i[0].split("=")[1]
                start = i[1].split("=")[1]
                end = i[2].split("=")[1]
                try:
                    op = SERVER + ext[
                        4] + chromo + ":" + start + "-" + end + '?feature=gene;content-type=application/json'
                    print(op)
                    conn = requests.get(op)
                    data = conn.json()
                    l = "<ul>"

                    if len(data) != 0:
                        # adding one by one the genes
                        for i in data:
                            l += '<p>' "<li>" + i["external_name"] + "</li>" + "</p>"

                    # when the dictionary is empty, so the chromosome does not has this region
                    else:
                        l += "Sorry, chose another region"
                    l = l + """</ul></body></html>"""

                    contents = """<!DOCTYPE html> 
                                       <html lang="en"> 
                                       <head>
                                            <meta charset="UTF-8">
                                            <title>Sequence</title>
                                       </head>
                                       <body style="background-color: #F6D8FF;">
                                       <h1><b><FONT face = "Courier New">Gene List</FONT></b></h1>
                                       <a href="/"> Main page </a>
                                       <hr> 
                                       <p>Selected chromosome: {} </P>
                                       <p>Start: {} </P>
                                       <p>End: {} </P>
                                       <p> Gene list: {}</p>"""
                    # add to the html file
                    contents = contents.format(chromo, start, end, l)

                except TypeError:
                    contents = """<!DOCTYPE html> 
                                              <html lang="en"> 
                                              <head>
                                                   <meta charset="UTF-8">
                                                   <title>Error</title>
                                              </head>
                                              <body style="background-color: #FE2E2E;">
                                              <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                              <a href="/"> Main page </a>
                                              <hr>
                                              <p> Please enter a valid combination </p>
                                              </body>
                                              </html>"""

                except IndexError:
                    contents = """<!DOCTYPE html> 
                                              <html lang="en"> 
                                              <head>
                                                   <meta charset="UTF-8">
                                                   <title>Error</title>
                                              </head>
                                              <body style="background-color: #FE2E2E;">
                                              <h1><b><FONT face = "Courier New">ERROR</FONT></b></h1>
                                              <a href="/"> Main page </a>
                                              <hr>
                                              <p> Please enter a valid combination </p>
                                              </body>
                                              </html>"""

            else:
                self.send_response(404)
                with open('Error.html', 'r') as f:
                    for i in f:
                        contents += i
                        contents = str(contents)

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()

        # Response message
        self.wfile.write(str.encode(contents))


# Main program
with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("serving at port {}".format(PORT))

    try:

        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
