import socket
import os

#  Socket creation
s = socket.socket()
s.bind(("192.168.43.22",9999))
s.listen(5)

print('socket created')

print('waiting for connections')


def do_service():
    c, address = s.accept()
    print('Connected with ', address)
    # Accept connections

    while True:
        request = c.recv(1024).decode()

        if request[:5] == 'locn:':
            if '$' not in request[5:]:
                send_files(c, request[5:])

    c.send('Hi dude'.encode())
    print('service executed')
    c.close()


def send_files(c, dire):
    for file in os.listdir(dire):
        print(file)
        c.send(file.encode())
        c.send('&'.encode())
    c.send('endlast'.encode())


do_service()
