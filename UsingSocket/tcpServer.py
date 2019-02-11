import json
import socket
from difflib import get_close_matches
def Main():
    host = "127.0.0.1"
    port = 8050

    s = socket.socket()
    # bind socket to a port
    s.bind((host,port))

    # he only listen in one con (every time)
    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    # Create dockerfile to write the code from requests
    dockerfile = open('Dockerfile', 'w')

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user :" + str(data))
        #write in file and at the end insert \n for new line
        dockerfile.write(str(data.decode()) + '\n')
	#send in client message 
        c.send("Data saved in Dockerfile".encode())
    dockerfile.close()
    c.close()


if __name__ == "__main__":
    Main()

