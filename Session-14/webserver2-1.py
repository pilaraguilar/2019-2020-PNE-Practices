import http.server
import socketserver

# Define the Server's port
PORT = 8081

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# we implement the class
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
def do_GET():
    """This method is called whenever the client invokes the GET method
    in the HTTP protocol request"""

    # We just print a message
    print("GET received!")

    # IN this simple server version:
    # We are NOT processing the client's request
    # We are NOT generating any response message
    return


class TestHandler(http.server.BaseHTTPRequestHandler):
    pass


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
