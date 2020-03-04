from Seq1 import Seq

import socket
import termcolor

#create the socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#to avoid a problem when a port is using

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP= "127.0.0.1"
PORT= 8081

#bind the socket to the servers ip and port

s.bind((IP,PORT))

#listen
s.listen()

print("Server is configured")

s0="TAGCTAGCTAAGCTAAAGCTTGACTAGA"
s1="ACTGACTAGTACGACTCAGCATAGTAGT"
s2="ATGCATTTGACTAGCTAGCATAGAACAT"
s3="ATTTGACATGCTTAGCTGACTAACCCAT"
s4="GTCAGTCAGTCCTGCAGGATCGATCAGA"





while True:
    #waiting for a client
    print("Waiting for a client connection")

    try:
        (cs, client_ip_port)=s.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")

        s.close()
        exit()

    else:

        #Read the message in bytes
        msg_raw = cs.recv(2048)

        # decode to read it properly
        msg = msg_raw.decode()

        l= msg.split(" ")


        if l[0]=="PING":
            termcolor.cprint("PING command", 'green')
            print("OK!\n")

        elif l[0]=="GET":
            termcolor.cprint("GET", 'green')

            if l[1]=="0":
                print(s0,  "\n")
                response = s0

            elif l[1]=="1":
                print(s1, "\n")
                response = s1

            elif l[1] == "2":
                print(s2,  "\n")
                response = s2

            elif l[1] == "3":
                print(s3,  "\n")
                response = s3

            elif l[1] == "4":
                print(s4, "\n")
                response = s4
            cs.send(response.encode())

        elif l[0]=="INFO":
            s=Seq(l[1])
            print("Sequence: ", s)
            print("Total lenght: ", s.len())
            for i in s:
                for b in ['A', 'C', 'T', 'G']:
                    print(b, ": ", s.seq_count_bases(b), end=", ")

                print()

        elif l[0]=="REV":
            s= S

        else:

            True


        # The message has to be in bytes


        cs.close()
