from Seq1 import Seq
from Seq0 import *

import socket
import termcolor

# create the socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# to avoid a problem when a port is using

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "127.0.0.1"
PORT = 8081

# bind the socket to the servers ip and port

s.bind((IP, PORT))

# listen
s.listen()

print("Server is configured")

s0 = "TAGCTAGCTAAGCTAAAGCTTGACTAGA"
s1 = "ACTGACTAGTACGACTCAGCATAGTAGT"
s2 = "ATGCATTTGACTAGCTAGCATAGAACAT"
s3 = "ATTTGACATGCTTAGCTGACTAACCCAT"
s4 = "GTCAGTCAGTCCTGCAGGATCGATCAGA"

while True:
    # waiting for a client
    print("Waiting for a client connection")

    try:
        (cs, client_ip_port) = s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        s.close()
        exit()

    else:

        # Read the message in bytes
        msg_raw = cs.recv(2048)

        # decode to read it properly
        msg = msg_raw.decode()

        li = msg.split(" ")

        if li[0] == "PING":
            termcolor.cprint("PING command", 'green')
            print("OK!\n")

        elif li[0] == "GET":
            termcolor.cprint("GET", 'green')

            if li[1] == "0":
                print(s0, "\n")
                response = s0
                cs.send(response.encode())

            elif li[1] == "1":
                print(s1, "\n")
                response = s1
                cs.send(response.encode())

            elif li[1] == "2":
                print(s2, "\n")
                response = s2
                cs.send(response.encode())

            elif li[1] == "3":
                print(s3, "\n")
                response = s3
                cs.send(response.encode())

            elif li[1] == "4":
                print(s4, "\n")
                response = s4
                cs.send(response.encode())

        elif li[0] == "INFO":
            termcolor.cprint("INFO", 'green')

            sequence = Seq(li[1])
            print("Sequence: ", sequence)
            print("Total lenght: ", sequence.len())
            counta = sequence.seq_count_bases('A')
            porta = (100 * counta / sequence.len())
            countc = sequence.seq_count_bases('C')
            portc = (100 * countc / sequence.len())
            countg = sequence.seq_count_bases('G')
            portg = (100 * countg / sequence.len())
            countt = sequence.seq_count_bases('T')
            portt = (100 * countt / sequence.len())

            print("A:", counta, "(", round(porta, 2), "%)")
            print("C:", countc, "(", round(portc, 2), "%)")
            print("G:", countg, "(", round(portg, 2), "%)")
            print("T:", countt, "(", round(portt, 2), "%)")

            response = f"""Sequence: {sequence}
            Total length: {sequence.len()}
            A: {counta} ({round(porta,2)}%)
            C: {countc} ({round(portc,2)}%)
            G: {countg} ({round(portg,2)}%)
            T: {countt} ({round(portt,2)}%)"""
            cs.send(response.encode())

        elif li[0] == "COMP":
            termcolor.cprint("COMP", 'green')
            sequence = Seq(li[1])
            comp = sequence.seq_complement()
            print(comp)
            cs.send(comp.encode())


        elif li[0] == "REV":
            termcolor.cprint("REV", 'green')
            sequence = Seq(li[1])
            rev = sequence.seq_reverse()
            cs.send(rev.encode())

        elif li[0] == "GENE":
            termcolor.cprint("GENE", 'green')
            gene = li[1]
            folder = "../session-04/"
            e = ".txt"
            seq = seq_read_fasta(folder + gene + e)
            print(seq)
            cs.send(seq.encode())

        else:
            True
            cs.close()
