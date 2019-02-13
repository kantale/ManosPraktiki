import json
import socket
import subprocess

def Main():
    host = "127.0.0.1"
    port = 8050

    s = socket.socket()
    # bind socket to a port
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host,port))

    # he only listen in one con (every time)
    s.listen(1)
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    communicateWithClient(s,c,addr)


def communicateWithClient(s,c,addr):
    while True:
        data = c.recv(2048)
        if not data:
            break
        if data.decode('utf-8') == 'b':
            print("recieved sudossss(bash) :    " + data.decode('utf-8'))
            data = c.recv(2048)
            r = execute(data.decode('utf-8'))
            jsfile = json.dumps(r)
            if jsfile:
                c.send(jsfile.encode())
        elif data.decode('utf-8') == 'w':
            print("recieved sudossss(without) :    " + data.decode('utf-8'))
            data = c.recv(2048)
            #subprocess.call('cd /dockerwithoutbash', shell=True)
            r = execute(data.decode('utf-8'))
            jsfile = json.dumps(r)
            if jsfile:
                c.send(jsfile.encode())
        elif data.decode('utf-8') == 'q':
            c.close()
        else:
            communicateWithClient(s,c,addr)




def execute(cm):
    process = subprocess.Popen(cm, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)

    out,err = process.communicate()
    errcode = process.returncode

    out = out.decode('utf-8')
    print("STDOUT : " + out)
    err = err.decode('utf-8')
    print("STDERR : " + err)

    print("ERROR CODE : "+ str(errcode))
    return {
            "stdout": out,
            "stderr": err,
            "error_code": errcode
    }


if __name__ == "__main__":
    Main()
