import json
import socket
import subprocess

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
    dockerfile = open('Dockerfile', 'r')

    while True:
        data = c.recv(1024)
        if not data:
            break
        print("from connected user :" + str(data))
        #write in file and at the end insert \n for new line
        #dockerfile.write(str(data.decode()) + '\n')
	#send in client message 
        c.send("Data saved in Dockerfile".encode())
    dockerfile.close()

    execute("sudo docker build -t testin/app .","building")
    execute("sudo docker run testin/app","running")

    c.close()



def execute(cm, typeofcommand):
    sudoPassword = 'tp4002'
    process = subprocess.Popen(cm, shell=True, stdout=subprocess.PIPE,
    stderr = subprocess.PIPE)
    passSudo = subprocess.Popen(sudoPassword, shell=True, stdout=subprocess.PIPE,
    stderr = subprocess.PIPE)

    out,err = process.communicate()
    errcode = process.returncode

    out = out.decode('utf-8')
    print(out + " " + typeofcommand)
    err = err.decode('utf-8')
    print(err + " " + typeofcommand)


if __name__ == "__main__":
    Main()

