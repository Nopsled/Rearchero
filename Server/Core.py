#!/usr/bin/env python
# sudo nodemon - -exec python Core.py
import random
import socket
import msgpack
from threading import Thread
import time
import ssl
import OpenSSL
from OpenSSL import crypto

class GameWorldManager:
    instances = []
    
    def broadcastWorldCommand():
        pass
            
    def getAllPlayers():
        pass
    
    def sendChatMessage():
        pass
class GameObject:
    def __init__(self, id=random.randint(0, 999), x=random.randint(0, 300), y=random.randint(0, 300), scale=random.randint(10,100), type=random.randint(0,3)):
        pass
        
    def __repr__(self):
        return f"{self.id},\n{self.x},\n{self.y},\n{self.unk1},\n{self.scale},\n{self.type},\n{self.unk4},\n{self.unk5}"
    
    def get(self):
        return [self.id, self.x, self.y, self.unk1, self.scale, self.type, self.unk4, self.unk5]
class PlayerObject:
    def __init__(self, socket, id=1, y=0, x=0, angle=0.0, usingItemID=1, unk2=0, unk3=0, unk4=None, clanLeader=0, skin=0, usingAccessoryID=0, showSkull=0, unk9=0):
        pass
        
    def setResource(self, resourceType="wood", amount=10):
        pass
                    
    def __repr__(self):
        pass
    
    def get(self):
        pass

# RC4Encrypter_pwdStr = "DusT0I+nh6FQUV2QonQoPUFnBeUNtFdtN284BDKWaP094CrB4E5R2i4GGDaxElWydqcaWLYyVdCZjRVl83iLmdTPjx/atbqCff35v8jKGQd8MMtgJjalbFsF4my9lEEL"
# Define the RC4 encryption algorithm
# def rc4(key, data):
#     S = [i for i in range(256)]
#     j = 0
#     for i in range(256):
#         j = (j + S[i] + key[i % len(key)]) % 256
#         S[i], S[j] = S[j], S[i]

#     i = j = 0
#     out = bytearray()
#     for byte in data:
#         i = (i + 1) % 256
#         j = (j + S[i]) % 256
#         S[i], S[j] = S[j], S[i]
#         k = S[(S[i] + S[j]) % 256]
#         encryptedByte = byte ^ k
#         print("Encrypted byte: " + str(encryptedByte))
#         out.append(encryptedByte)

#     return out
#Encrypt the data using the RC4 algorithm and key
# encrypted_data = rc4(key, data)


def generate_cert(common_name):
    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().CN = common_name
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(pkey)
    cert.sign(pkey, 'sha256')

    # Write the certificate to a file
    with open("cert.pem", "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    # Write the private key to a file
    with open("key.pem", "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey))

class Client:
    def __init__(self, socket):
        self.socket = socket
        self.port = self.socket.getsockname()[1]

    def recv(self):
        while True:
            time.sleep(0.1)
            
            try: 
                data = self.socket.recv(4096)
            except Exception as e:
                print(f'[-]: {e}')
                
            # try:
            #     data = self.socket.recv(1024).hex()
            # except Exception as e:
            #     print(f'[-]: {e}')

            if len(data) > 0:
                
                if self.port == 443:
                    print(f'[Recv (port:{self.port})]: {data}')
                    print('')
                
                self.socket.send(data)
                                  



def onNewClient(clientSocket, clientAddress, isSSL):
    client = Client(clientSocket)
    #GameWorldManager.instances.append(client)
    Thread(target=client.recv).start()
    #Thread(target=client.gameLoop).start()
    print(f'[+]: New game client connected: {clientAddress}')
    

def loop(socket, port, isSSL):
    print(f'[+] Server started 0.0.0.0:{port}. Waiting for connections...')
    while True:
        (clientSocket, clientAddress) = socket.accept()
        if isSSL == True: clientSocket = context.wrap_socket(clientSocket, server_side=True)

        onNewClient(clientSocket, clientAddress, isSSL)


if __name__ == "__main__":   

    # Generate a private key
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)

    # Generate the certificate
    generate_cert("mail-archero.habby.mobi")


    # 9952, 8080, (443)
    ports = []
    sockets = [
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ]

    sslPort = 443
    
    for s in sockets:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    sslSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslSocket.bind(("0.0.0.0", sslPort))
    sslSocket.listen(5)
    
    # wrap the socket with SSL/TLS
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    Thread(target=loop, args=(sslSocket, sslPort, True,)).start()
    
    for i in range(len(sockets)):
        port = ports[i]
        s = sockets[i]
        s.bind(("0.0.0.0", port))
        s.listen(5)
        Thread(target=loop, args=(s, port, False,)).start()