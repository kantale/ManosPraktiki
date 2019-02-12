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
        if not data or data.decode() == '+q':
            break
        print("from connected user :" + data.decode())
        #write in file and at the end insert \n for new line
        #dockerfile.write(str(data.decode()) + '\n')
	#send in client message
        if data.decode() == '+r':
            c.send("Which container : ".encode())
            data = c.recv(1024)
            execute("sudo docker run " + data.decode())
        elif data.decode() == '+w':
            c.send("Give name for the container : ".encode())
            data = c.recv(1024)
            execute("sudo docker build -t " + data.decode() + " .")
            execute("sudo docker run " + data.decode())

    dockerfile.close()

    c.close()



def execute(cm):
    # insert you code here
    sudoPassword = 'INSERT_YOUR CODE'
    process = subprocess.Popen(cm, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)
    passSudo = subprocess.Popen(sudoPassword, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)

    out,err = process.communicate()
    errcode = process.returncode

    out = out.decode('utf-8')
    print(out + " ")
    err = err.decode('utf-8')
    print(err + " ")


if __name__ == "__main__":
    Main()

