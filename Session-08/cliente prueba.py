import socket

ip = "127.0.0.1"

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mi_socket.connect(("127.0.0.1", 8080))
mi_socket.send(str.encode("Hola soy el cliente, yo inicio la conversación"))
response = mi_socket.recv(2000).decode("utf-8")

print(response)
mi_socket.close()
