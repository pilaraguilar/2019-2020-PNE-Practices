from Client0 import Client

#Implement the debug_talk() method.
# It just call the talk() method and prints both messages on the console, in different colors
PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.142"
PORT = 8080

c = Client(IP, PORT)
print(c)

c.debug_talk("Message 1---")
c.debug_talk("Message 2: Testing !!!")