from helper import  *
import socket
import signal
def runClient(serverip,serverport,caip,caport):
    signal.signal(signal.SIGINT, signal_handler)
    print("client connecting to",serverip,serverport,caip,caport)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
        client.connect((serverip, serverport))
        while True:#run in a infinite loop and take input until user press ctrl c
            # take input
            data=input()
            # encrypt the input then send it in the form of bytes
            encryptedData=encrypt("encrypt using server public key",data)
            client.sendall(encryptedData.encode())

            #receive the acknowledgement from the server, decrypt it and then decode it from the byte form
            data=client.recv(2048)
            data=decrypt("decrypt using your own private key",data)
            print(data.decode())

    return 0

if __name__=="__main__":
    runClient('127.0.0.1',9090,"",8080)