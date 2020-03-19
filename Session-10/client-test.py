from Client0 import Client

PORT = 8080
IP = "127.0.0.1"

for number in range(5):
    connection = Client(IP, PORT)
    print("Message", connection.debug_talk(number))
