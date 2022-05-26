# Connect to the server and send a message
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

# Connect to the server
s.connect((host, port))

# Send the message
message = "Hello, World!"
