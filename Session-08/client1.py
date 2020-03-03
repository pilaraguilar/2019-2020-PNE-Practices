import socket
# is already installed

IP = "212.128.253.143"
PORT = 8080


# we create the socket

#the socket is an object to send info
#we always have to use AF_INET (internet socket)  and SOCK_STREAM (type of info)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #the first in the name of the module and inside it we have a class called socket

# we connect the socket with the server
s.connect((IP, PORT))

# send info for the socket, only bytes
s.send(str.encode("holaa silvia")) #in bytes

# receive data from the server
msg = s.recv(2000).decode("utf-8") #2000 is the maximum value of bytes we want to receive from the server

print("Message from the server: ", msg)

# closing the connection
s.close()
