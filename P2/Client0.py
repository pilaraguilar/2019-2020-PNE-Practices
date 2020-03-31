# in this exercise we connect to our computer, poniendo en el terminal "nc -l" y sale el mensaje


import socket
import termcolor


def ping():  # a function that only prints ok
    print("OK!")


class Client:

    def __init__(self, ip, port):
        # function for initializing the object
        # strsbases : is a parameter, you can call wherever you want
        self.ip = ip  # passed as an argument when creating the object
        self.port = port

    def __str__(self):  # it gives the internal info of the object
        return f"Connection to SERVER at {self.ip} , PORT: {self.port}"

    def talk(self, msg):
        # -- Create the socket
        # socket is the name of the module and the class
        # inside the braquets internet socket and type of info
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))


        # Receive data
        response = s.recv(2048).decode("utf-8")
      # blue color
        # Close the socket
        s.close()

        # Return the response
        return response

    def debug_talk(self, m_from_server):  # response message from the server
        m_from_server = self.talk(m_from_server)
        print("From Server: ", end="")
        termcolor.cprint(m_from_server, "green")
        return m_from_server
