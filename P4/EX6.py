import socket
import termcolor
from pathlib import Path

# -- Server network parameters
IP = "127.0.0.1"
PORT = 8080


def get_re(path):
    code = 200
    if path == "/info/A":
        resp = Path("A.html").read_text()
    elif path == "/info/C":
        resp = Path("C.html").read_text()
    elif path == "/info/G":
        resp = Path("G.html").read_text()
    elif path == "/info/T":
        resp = Path("T.html").read_text()
    elif path == "/":
        resp = Path("index.html").read_text()
    else:
        resp = Path("Error.html").read_text()
        code = 404

    return resp, code


def process_client(s):
    # -- Receive the request message
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print("Message FROM CLIENT: ")

    # -- Split the request messages into lines
    lines = req.split('\n')

    # -- The request line is the first
    req_line = lines[0]

    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")

    # -- Process the request line
    words = req_line.split(' ')

    # -- Get the method and path
    method = words[0]

    print("Method:", method)

    # -- Response body
    # -- Initially it is blank
    resp_body = ""
    code = 0

    if method == "GET":
        path = words[1]
        resp_body, code = get_re(path)

    if code == 200:
        status = "ok"
    else:
        status = "Not found 404"

    # -- Status line: We respond that everything is ok (200 code)
    status_line = f"HTTP/1.1 {code} {status}\n"

    # -- Add the Content-Type header
    header = "Content-Type: text/html\n"

    # -- Add the Content-Length
    header += f"Content-Length: {len(resp_body)}\n"

    # -- Build the message by joining together all the parts
    response_msg = status_line + header + "\r\n" + resp_body
    cs.send(response_msg.encode())


# -------------- MAIN PROGRAM
# ------ Configure the server
# -- Listening socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Setup up the socket's IP and PORT
ls.bind((IP, PORT))

# -- Become a listening socket
ls.listen()

print("SEQ Server configured!")

# --- MAIN LOOP
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:

        # Service the client
        process_client(cs)

        # -- Close the socket
        cs.close()
