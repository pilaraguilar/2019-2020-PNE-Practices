from Client0 import Client, ping

PRACTICE = 2
EXERCISE = 1

print("-----| Practice ", PRACTICE, "Exercise" , EXERCISE , "|------")

# -- Parameters of the server to talk to
IP = "127.0.0.1"  #the ip of my computer
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Test the ping method
ping()

# -- Print the IP and PORTs
print(f"IP: {c.ip}, {c.port}")