from helper import *
import socket
import signal
HOST='127.0.0.1'
signal.signal(signal.SIGINT,signal_handler)
def acceptConnection(server,port ,caip,caport):
    connection, addr = server.accept()
    with connection:

        # hardcoded value for testing
        id = 8080 if port == 9090 else 9090
        getPublicKeyFromCA(caip,caport,id)

        print("client connected. address:", addr)
        print(connection)
        i = 1
        while True:


            # receive data from the connection first decode it from the bytes to text and then decrypt it
            encrypted_data = connection.recv(2048)
            data = decrypt(getPrivateKey("8080"), encrypted_data)
            print(data)

            # first encrypt the acknowledgement and then send it back to the sender in the form of bytes
            ack = encrypt(getPublicKey("9090"), "ack " + str(i))
            connection.sendall(ack)
            i = i + 1
def runServer(port,caip,caport):



    print("server running on port" , port)

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.bind((HOST,port))
        server.listen(5)
        while True:
            try :
                acceptConnection(server,port,caip,caport)
            except:
                print("connection closed")



    return 0


if __name__=="__main__":
    runServer(8080,"127.0.0.1",8081)