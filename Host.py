import socketserver

s = socketserver.TCPServer(('', 8080), socketserver.BaseRequestHandler)
s.serve_forever()

# Print server address
print(s.server_address)

# Print connected client address
print(s.RequestHandlerClass.rfile.client_address)

