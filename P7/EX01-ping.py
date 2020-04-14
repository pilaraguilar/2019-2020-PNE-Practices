import http.client


PORT = 8080
server = 'rest.ensembl.org'
endpoint = '/info/ping'
params = '?content-type=application/jsonp'
URL = server + endpoint + params
print("SERVER:", server)
print("URL:", URL)


# Connect with the server
conn = http.client.HTTPConnection(server, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", endpoint + params)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Print the received data
print(f"CONTENT: {data1}")
