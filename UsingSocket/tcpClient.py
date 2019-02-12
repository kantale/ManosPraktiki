import socket

def Main():
    host = "127.0.0.1"
    port = 8050

    s = socket.socket()
    s.connect((host,port))

    message = input("Give +w (install container) or +r (run container) : ")
    while message != 'q':
        if message == '+r':
            s.send(message.encode())
            data = s.recv(1024)
            print("Recieved from server :" + str(data))
            message =input("-> ")
            s.send(message.encode())
        elif message == '+w':
            s.send(message.encode())
            data = s.recv(1024)
            print("Recieved from server :" + str(data))
            message =input("-> ")
            s.send(message.encode())
        else:
            break
    s.close()



if __name__ == "__main__":
    Main()


