import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "127.0.0.1"          # Get local machine name
port = 8080                # Reserve a port for your service.

s.connect((host, port))
print (s.recv(1024))
s.close()  
