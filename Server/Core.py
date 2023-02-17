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
        

PACKET_DATA ="""
message: {'type': 'send', 'payload': '[HOOKED: Encrypt_UTF8]: "{"helpEggIds":[],"offlineList":[],"onlineList":[],"twoRoomId":"","twoRoomTime":0,"complaintList":[],"appealList":[]}" using password: "4ptjerlkgjlk34jylkej4rgklj4klyj"'} data: None
Password: 4ptjerlkgjlk34jylkej4rgklj4klyj

message: {'type': 'send', 'payload': '[HOOKED: DesDecrypt]: "A+w0px8qcpvV9aCkoQx71fsuk4vRYOpoUWEZfon1PT1K4UJm+pVwCkgTI2q5YSZ70oxmYCurFjfZnEi2WuO2eeO7N5yw/cDZBkWtXiYUiZ8=" using password: "BLanr2GPVfp6JNXktzBLanr2GPVfp6JN"'} data: None
"""

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
        

#Packet 1 [C -> S]: Directly after connection:
# Data:  b'\x00\x00\x00\x1a\x014a\xcd\x87\xe1\x03\xa2\tOS.Hello\x01\x00\x00\x00\x00'
# Data:  b'\x00\x00\x00\x1a\x014a\xcd\x87\xe1\x03\xa4\tOS.Hello\x01\x00\x00\x00\x00'
# Data:  b'\x00\x00\x00\x1a\x014a\xcd\x87\xe1\x03\xa5\tOS.Hello\x01\x00\x00\x00\x00'

# RC4Encrypter_pwdStr = "DusT0I+nh6FQUV2QonQoPUFnBeUNtFdtN284BDKWaP094CrB4E5R2i4GGDaxElWydqcaWLYyVdCZjRVl83iLmdTPjx/atbqCff35v8jKGQd8MMtgJjalbFsF4my9lEEL"

# Key as string
pwdStr = "DusT0I+nh6FQUV2QonQoPUFnBeUNtFdtN284BDKWaP094CrB4E5R2i4GGDaxElWydqcaWLYyVdCZjRVl83iLmdTPjx/atbqCff35v8jKGQd8MMtgJjalbFsF4my9lEEL"

# byte 68 = char D in decimal

# key = [68, 117, 115, 84, 48, 73, 43, 110, 104, 54, 70, 81, 85, 86, 50, 81, 111, 110, 81, 111, 80, 85, 70, 110, 66, 101, 85, 78, 116, 70, 100, 116, 78, 50, 56, 52, 66, 68, 75, 87, 97, 80, 48, 57, 52, 67, 114, 66, 52, 69, 53, 82, 50, 105, 52, 71, 71, 68, 97, 120, 69, 108, 87, 121,
#        100, 113, 99, 97, 87, 76, 89, 121, 86, 100, 67, 90, 106, 82, 86, 108, 56, 51, 105, 76, 109, 100, 84, 80, 106, 120, 47, 97, 116, 98, 113, 67, 102, 102, 51, 53, 118, 56, 106, 75, 71, 81, 100, 56, 77, 77, 116, 103, 74, 106, 97, 108, 98, 70, 115, 70, 52, 109, 121, 57, 108, 69, 69, 76]
# data = [151, 61, 177, 75, 33, 232, 181, 124, 228, 210, 166, 219, 168, 216, 39, 226, 52, 17, 248, 33, 169, 119, 115, 242, 238, 195, 155, 138, 179, 113, 25, 234, 32, 142, 71, 240, 9, 0, 140, 231, 222, 196, 157, 192, 29, 5, 197, 34, 206, 161, 228, 93, 154, 64, 171, 7, 39, 61, 167, 113, 162, 201, 114, 233, 166, 251, 87,
#         230, 184, 41, 190, 131, 116, 151, 40, 119, 201, 48, 211, 1, 3, 107, 214, 177, 74, 54, 154, 138, 166, 130, 202, 196, 145, 109, 123, 66, 108, 224, 154, 26, 32, 95, 207, 202, 1, 16, 205, 55, 115, 10, 139, 86, 205, 201, 191, 44, 120, 99, 213, 80, 1, 253, 8, 114, 132, 143, 219, 117, 106, 223, 47, 80, 148, 47, 197, 10]

# # Define the RC4 encryption algorithm


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


# # Encrypt the data using the RC4 algorithm and key
# encrypted_data = rc4(key, data)

# # Print the encrypted data
# print("Encrypted Data:", encrypted_data)

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


    sockets = [
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ]
    # 9952, 8080, 443
    ports = [9952, 8080]
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