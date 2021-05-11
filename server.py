import socket

#variables
HOST = socket.gethostbyname(socket.gethostname()) #It returns your local IP address
PORT = 5050
ADDR = (HOST,PORT)
BUFFER_SIZE = 1024*128

#Create TCP Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

#Client Handler
def client_handler(conn, addr):
    while 1:
        cwd = conn.recv(BUFFER_SIZE).decode('utf-8')
        print("( {0}:{1} )".format(addr[0],addr[1]),cwd+"> ",end='')
        command = input().encode('utf-8')
        conn.send(command)
        print(conn.recv(BUFFER_SIZE).decode('utf-8'))
        print()

def start():
    while True:
        conn, addr = server.accept()
        client_handler(conn,addr)
    


print("[STARTING] server is starting...")
start()

