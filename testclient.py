import socket
s=socket.socket()
s.connect(('192.168.43.152',6875))
name=input('Enter name')
s.send(bytes(name,'utf-8'))
while(True):
    st=s.recv(1024).decode()
    if not st:
        break
    print(st)
