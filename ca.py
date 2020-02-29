import socket
from helper import *
import signal
HOST='127.0.0.1'


def runca(port):
    signal.signal(signal.SIGINT, signal_handler)
    print("ca running on port",port)

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ca_server:
        ca_server.bind((HOST,port))
        ca_server.listen(5)
        while True:
            connection,addr=ca_server.accept()

            with connection:
                print("client connected address",addr)

                # since this data for generating and sending public key , this will be in json format
                id=connection.recv(4096)
                jsonCertificate=createCertificate(id)
                connection.sendall(jsonCertificate.encode())
                connection.close()