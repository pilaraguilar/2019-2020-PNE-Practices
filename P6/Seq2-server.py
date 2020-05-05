import socketserver
import termcolor
from Seq1 import Seq
from pathlib import Path
import http.server

# Define the Server's port
PORT = 8001

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

seq_list = ["ACTGATCTAGAAAACTCGATCA",
    "ATGACTAGATTATACTGGATTC",
    "GCTAGCTAGCTTATATACGTAT",
    "TAGCTTAGTTACGATCAGTAGA",
    "ATGTAGCTTAGTCAGTACATGA"]

FOLDER = "../session-04/"
EXT = ".txt"


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the request line
        req_line = self.requestline.split(' ')

        # Get the path. It always start with the / symbol
        path = req_line[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML
        contents = Path('Error.html').read_text()
        error_code = 404

        if verb == "/":
            # Open the form1.html file
            # Read the index from the file
            contents = Path('form-4.html').read_text()
            error_code = 200
        elif verb == "/ping":
            contents = """
            <!DOCTYPE html>
            <html lang = "en">
            <head>
            <meta charset = "utf-8" >
              <title> PING </title >
            </head >
            <body>
            <h2> PING OK!</h2>
            <p> The SEQ2 server in running... </p>
            <a href="/">Main page</a>
            </body>
            </html>
            """
            error_code = 200
        elif verb == "/get":
            # the right of the ? symbol
            pair = arguments[1]
            #  name = value
            pairs = pair.split('&')
            #  name and value
            name, value = pairs[0].split("=")
            n = int(value)

            # Get the sequence
            seq = seq_list[n]

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GET </title >
                        </head >
                        <body>
                        <h2> Sequence number {n}</h2>
                        <p> {seq} </p>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200
        elif verb == "/gene":
            #  right of the ? symbol
            pair = arguments[1]
            #  name = value
            pairs = pair.split('&')
            #  name and value
            name, gene = pairs[0].split("=")

            s = Seq()
            s.seq_read_fasta(FOLDER + gene + EXT)
            gene_str = str(s)

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> GENE </title >
                        </head >
                        <body>
                        <h2> Gene: {gene}</h2>
                        <textarea readonly rows="60" cols="80"> {gene_str} </textarea>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200
        elif verb == "/operation":
            #  the right of the ? symbol
            pair = arguments[1]
            #  name = value
            pairs = pair.split('&')
            #  name and value
            name, seq = pairs[0].split("=")
            #  elements of the operation
            name, op = pairs[1].split("=")

            s = Seq(seq)

            if op == "comp":
                result = s.seq_complement()
                op = "complementary"
            elif op == "rev":
                result = s.seq_reverse()
                op = "reverse"
            else:
                op = "information"
                sl = s.len()
                counta = s.seq_count_bases('A')
                porta = "{:.1f}".format(100 * counta / sl)
                countc = s.seq_count_bases('C')
                portc = "{:.1f}".format(100 * countc / sl)
                countg = s.seq_count_bases('G')
                portg = "{:.1f}".format(100 * countg / sl)
                countt = s.seq_count_bases('T')
                portt = "{:.1f}".format(100 * countt / sl)

                result = f"""
                <p>Total length: {sl}</p>
                <p>A: {counta} ({porta}%)</p>
                <p>C: {countc} ({portc}%)</p>
                <p>G: {countg} ({portg}%)</p>
                <p>T: {countt} ({portt}%)</p>"""

            contents = f"""
                        <!DOCTYPE html>
                        <html lang = "en">
                        <head>
                        <meta charset = "utf-8" >
                          <title> sequence </title >
                        </head >
                        <body>
                        <h2> Sequence </h2>
                        <p>{seq}</p>
                        <h2> Operation: </h2>
                        <p>{op}</p>
                        <h2> Result: </h2>
                        <p>{result}</p>
                        <br>
                        <br>
                        <a href="/">Main page</a>
                        </body>
                        </html>
                        """
            error_code = 200

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


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
        print("Stoped by the user")
        httpd.server_close()
