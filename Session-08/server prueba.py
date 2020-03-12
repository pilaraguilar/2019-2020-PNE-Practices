import socket

# SERVER IP, PORT
PORT = 8080
IP = "127.0.0.1"  # my ip

# -- Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((IP, PORT))  # vincularlo

s.listen(50)
while True:
    # accepting the request of the clients
    # clientsocket is the conexion
    (clientsocket, address) = s.accept()
    print("Nueva conexion")
    print(address)
    clientsocket.send(str.encode("Hola, como estas, te saludo del el servidor"))
    clientsocket.close()
