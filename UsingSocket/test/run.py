
import json
import subprocess

def execute(cm):
    # insert you code here
    #sudoPassword = 'INSERT_YOUR CODE'
    process = subprocess.Popen(cm, shell=True, stdout=subprocess.PIPE,stderr = subprocess.PIPE)

    out,err = process.communicate()
    errcode = process.returncode

    out = out.decode('utf-8')
    print("STDOUT:")
    print (out)

    err = err.decode('utf-8')
    print ("STDERR")
    print (err)


    print ("ERROR CODE:", errcode)

    return {
            "stdout": out,
            "stderr": err,
            "error_code": errcode,
    }

if __name__ == '__main__':
    command = "docker build ."
    r = execute(command)

    j = json.dumps(r)
    print (j)




