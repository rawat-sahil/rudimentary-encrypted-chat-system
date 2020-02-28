from helper import *
import socket
import signal
HOST='127.0.0.1'
def runServer(port):
    signal.signal(signal.SIGINT,signal_handler)
    print("server running on port" , port)
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((HOST,port))
        server.listen(5)
        connection,addr=server.accept()
        with connection:
            print("client connected. address:",addr)
            i=1
            while True:
                # receive data from the connection first decode it from the bytes to text and then decrypt it
                data=connection.recv(2048)
                data=decrypt("decrypt using your private key",data.decode())
                print(data)

                # first encrypt the acknowledgement and then send it back to the sender in the form of bytes
                ack=encrypt("encrypt using the public key","ack "+str(i) )
                connection.sendall(ack.encode())
                i=i+1

    return 0


if __name__=="__main__":
    runServer(8080)