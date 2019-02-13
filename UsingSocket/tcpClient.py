import json
import socket

def Main():
    host = "127.0.0.1"
    port = 8050

    s = socket.socket()
    s.connect((host,port))

    message = input("with bash(b) or without(w)->")
    while message != 'q' or command != 'q':
        if message == 'b':
            s.send(message.encode())
            command = input("->")
            s.send(command.encode())
            data = s.recv(25000)
            jdata = data.decode('utf-8')
            if jdata :
                print(jdata)
                break
        elif message == 'w':
            s.send(message.encode())
            command = input("->")
            s.send(command.encode())
            data = s.recv(25000)
            jdata = data.decode('utf-8')
            if jdata :
                print(jdata)
                break
    s.close()


if __name__ == "__main__":
    Main()


