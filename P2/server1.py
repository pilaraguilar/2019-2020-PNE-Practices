import socket


# SERVER IP, PORT
PORT = 8080
IP =  "172.20.10.2"  #my ip

# -- Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP,PORT)) #vincularlo

s.listen(50)
while True:

    (clientsocket, address) = s.accept()

    #read the message from the client
    #the server waits to the message to arrive
    m= clientsocket.recv(2100)

    print("Message from the client: ", end="")

    message = "\nHelloo\n"
    send_bytes = str.encode(message)

    # We must write bytes, not a string
    clientsocket.send(send_bytes)

    # -- Finish the connection
    clientsocket.close()

