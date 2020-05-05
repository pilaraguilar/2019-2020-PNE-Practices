from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print("-----| Practice", PRACTICE, "Exercise ", EXERCISE ," |------")

IP = "127.0.0.1"
PORT = 8085

c = Client(IP, PORT)
print(c)

# Ping
print(" Testing PING...")
print(c.talk("PING"))

# Get
print(" Testing GET...")
for i in range(5):
    cmd = f"GET {i}"
    print(cmd, ":",  c.talk(cmd), end="")

# INFO
seq = c.talk("ACTAGATTA")
print()
print(" Testing INFO...")
cmd = f"INFO {seq}"
print(c.talk(cmd))

# COMP
print(" Testing COMP...")
cmd = f"COMP {seq}"
print(cmd, end="")
print(c.talk(cmd))

# REV
print(" Testing REV...")
cmd = f"REV {seq}"
print(cmd, end="")
print(c.talk(cmd))

# GENE
print(" Testing GENE...")
for gene in ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P.txt"]:
    cmd = f"GENE {gene}"
    print(cmd)
    print(c.talk(cmd))

