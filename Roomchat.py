import time, socket , sys

socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080

print('This is your IP address ',ip)
server_host = input('Enter friend\'s IP address :')
name = input('Enter Friend\'s name :')

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.revc(1024)
server_name = server_name.decode() 

print(server_name,'has joined....' )
while True:
    messege = (socket_server.revc(1024)).decode()
    print(server_name,":", messege)
    messege = input("Me : ")
    socket_server.send(messege.encode())
