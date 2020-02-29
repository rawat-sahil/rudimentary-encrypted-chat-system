from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signer_PKCS1_v1_5
from datetime import  datetime
from Crypto.Hash import SHA256
import socket
import json
def signal_handler(signal,frame):
    exit(0)

def getPrivateKey(id):
    file=open(str(id)+"/"+str(id)+".priv","r")
    text=file.readlines()
    privatkey="".join(text)
    return privatkey

def getPublicKey(id):
    file = open(str(id)+"/"+str(id)+".pub", "r")
    text=file.readlines()
    publicKey="".join(text)
    return publicKey

def generateSignature(certificate):
    # certificate is list of parameters
    certContent="".join(certificate)
    digest=SHA256.new(certContent.encode())
    privateKey=getPrivateKey("ca")
    key=RSA.importKey(privateKey)
    signer=Signer_PKCS1_v1_5.new(key)
    sign=signer.sign(digest)
    return list(sign)


def verifyCertificate(certificate):
    # convert json certificate to cert
    cert=json.loads(certificate)
    digest=SHA256.new(("".join(i for i in cert[:3])).encode())
    publicKey=getPublicKey("ca")
    key=RSA.importKey(publicKey)
    verifier=Signer_PKCS1_v1_5.new(key)
    verified=verifier.verify(digest,bytes(cert[3]))
    return verified

def createCertificate(id):
    requestedPublicKey = getPublicKey(id)
    certificate=[]
    certificate.append(id)
    certificate.append(requestedPublicKey)
    certificate.append(datetime.now().__str__())
    certificate.append(generateSignature(certificate))
    return json.dumps(certificate)

def extractPublicKeyFromCertificate(certificate):
    cert=json.loads(certificate)
    return cert[1]


def getPublicKeyFromCA(caip,caport,id):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
        client.connect((caip,caport))
        client.sendall(str(id).encode())
        Jsoncertificate=client.recv(2048).decode()
        client.close()
        if verifyCertificate(Jsoncertificate):
            return extractPublicKeyFromCertificate(Jsoncertificate)
        else :
            exit(0)

def encrypt(key,plain_text):
    pubickey=RSA.importKey(key)
    cipher=Cipher_PKCS1_v1_5.new(pubickey)
    cipher_text=cipher.encrypt(plain_text.encode())
    return cipher_text

def decrypt(key,cipher_text):
    privateKey=RSA.importKey(key)
    cipher=Cipher_PKCS1_v1_5.new(privateKey)
    plain_text=cipher.decrypt(cipher_text,None).decode()
    return plain_text


if __name__=="__main__":
    a=createCertificate("8080")
    verifyCertificate(a)