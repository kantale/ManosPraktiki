import json
import socket

def Main():
    host = "127.0.0.1"
    port = 8050
    s = socket.socket()
    s.connect((host,port))
    communicateWithServer(s)


def communicateWithServer(s):
    message = input("with bash(b) or without(w)->")
    while message != 'q':
        if message == 'b':
            s.send(message.encode())
            message = input("->")
            s.send(message.encode())
            data = s.recv(25000)
            jdata = data.decode('utf-8')
            if jdata :
                print(jdata)
        elif message == 'w':
            s.send(message.encode())
            message = input("->")
            s.send(message.encode())
            data = s.recv(25000)
            jdata = data.decode('utf-8')
            if jdata :
                convjson = json.loads(jdata)
                print(convjson)
        else:
            communicateWithServer(s)
    s.close()

if __name__ == "__main__":
    Main()


