#!/usr/bin/env python
# sudo nodemon - -exec python Core.py
import random
import socket
import msgpack
from threading import Thread
import time
import ssl
import OpenSSL
import subprocess
from OpenSSL import crypto

# enable/disable proxy:
# adb shell settings put global http_proxy 127.0.0.1: 8889
# or dynamically taking my pc as host
# adb shell settings put global http_proxy $(ipconfig getifaddr en0): 8888
# To disable that proxy use:
# adb shell settings put global http_proxy: 0

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


cert_str = """
-----BEGIN CERTIFICATE-----
[
[
  Version: V3
  Subject: CN=habby.mobi
  Signature Algorithm: SHA256withRSA, OID = 1.2.840.113549.1.1.11

  Key:  Sun RSA public key, 2048 bits
  params: null
  modulus: 26000169808348282176637874931097892150273366304155500275594083360835736836470538900877738517719909397469192852162353833534564443945066199830902644319587329097344859001508480948411433453208845376381394754087512216029460237609525032268001907939463247276557136825989256670471297181212656747211434657278807944781668500228858488660016893582286402415790762855110150237355481015565442913699835328800351418934598762372006272944058157959328198165133934245192738006469871216627164585353380570130400164725446619579865419279228341647968000892133096363884020833707723486285632646809894689747409737501323141568383582636859861974521
  public exponent: 65537
  Validity: [From: Wed Aug 17 02:00:00 CEST 2022,
               To: Fri Sep 15 01:59:59 CEST 2023]
  Issuer: CN=Amazon, OU=Server CA 1B, O=Amazon, C=US
  SerialNumber: [    02c0c2b6 bdb5dde2 43682595 86c80f27]

Certificate Extensions: 10
[1]: ObjectId: 1.3.6.1.4.1.11129.2.4.2 Criticality=false
Extension unknown: DER encoded OCTET string =
0000: 04 82 01 6C 04 82 01 68   01 66 00 75 00 E8 3E D0  ...l...h.f.u..>.
0010: DA 3E F5 06 35 32 E7 57   28 BC 89 6B C9 03 D3 CB  .>..52.W(..k....
0020: D1 11 6B EC EB 69 E1 77   7D 6D 06 BD 6E 00 00 01  ..k..i.w.m..n...
0030: 82 AA 88 FF C8 00 00 04   03 00 46 30 44 02 20 2D  ..........F0D. -
0040: F6 43 25 DE A1 A8 5F D7   59 5F D3 04 3E 86 D5 22  .C%..._.Y_..>.."
0050: 08 3A FC F1 CE 61 17 9A   69 BA BB 17 72 9B 32 02  .:...a..i...r.2.
0060: 20 4D B3 22 AB B7 67 D8   92 78 96 24 D2 87 55 C9   M."..g..x.$..U.
0070: 2D 47 3D 4C A2 FF 05 65   DB C1 9D 28 B6 E4 87 CE  -G=L...e...(....
0080: 03 00 76 00 B3 73 77 07   E1 84 50 F8 63 86 D6 05  ..v..sw...P.c...
0090: A9 DC 11 09 4A 79 2D B1   67 0C 0B 87 DC F0 03 0E  ....Jy-.g.......
00A0: 79 36 A5 9A 00 00 01 82   AA 89 00 2B 00 00 04 03  y6.........+....
00B0: 00 47 30 45 02 21 00 AC   FA 4E 98 7F 07 E3 47 68  .G0E.!...N....Gh
00C0: B7 B7 B9 F0 13 EF D3 1C   9B FE FC BA 59 97 EE 89  ............Y...
00D0: 2B DB BD 35 23 85 68 02   20 6E FB C5 92 C1 53 AE  +..5#.h. n....S.
00E0: E4 BD EE 34 4E 65 52 37   26 DC 04 5F FD 14 2D 76  ...4NeR7&.._..-v
00F0: BC 1B EB 24 4C 13 71 C0   EE 00 75 00 B7 3E FB 24  ...$L.q...u..>.$
0100: DF 9C 4D BA 75 F2 39 C5   BA 58 F4 6C 5D FC 42 CF  ..M.u.9..X.l].B.
0110: 7A 9F 35 C4 9E 1D 09 81   25 ED B4 99 00 00 01 82  z.5.....%.......
0120: AA 89 00 02 00 00 04 03   00 46 30 44 02 20 4B 1C  .........F0D. K.
0130: 34 65 48 1A AC F8 FA F4   68 1F 60 11 45 D5 D6 89  4eH.....h.`.E...
0140: 52 AC B1 A5 67 D5 2F 07   E8 77 63 C6 7D D1 02 20  R...g./..wc.... 
0150: 68 88 00 7C 7F 92 C9 5B   DC AC 24 44 AA 10 05 E4  h......[..$D....
0160: 1C 1C EF 91 B4 9B F6 9E   79 49 E2 73 E2 5D D9 B8  ........yI.s.]..


[2]: ObjectId: 1.3.6.1.5.5.7.1.1 Criticality=false
AuthorityInfoAccess [
  [
   accessMethod: ocsp
   accessLocation: URIName: http://ocsp.sca1b.amazontrust.com
, 
   accessMethod: caIssuers
   accessLocation: URIName: http://crt.sca1b.amazontrust.com/sca1b.crt
]
]

[3]: ObjectId: 2.5.29.35 Criticality=false
AuthorityKeyIdentifier [
KeyIdentifier [
0000: 59 A4 66 06 52 A0 7B 95   92 3C A3 94 07 27 96 74  Y.f.R....<...'.t
0010: 5B F9 3D D0                                        [.=.
]
]

[4]: ObjectId: 2.5.29.19 Criticality=true
BasicConstraints:[
  CA:false
  PathLen: undefined
]

[5]: ObjectId: 2.5.29.31 Criticality=false
CRLDistributionPoints [
  [DistributionPoint:
     [URIName: http://crl.sca1b.amazontrust.com/sca1b-1.crl]
]]

[6]: ObjectId: 2.5.29.32 Criticality=false
CertificatePolicies [
  [CertificatePolicyId: [2.23.140.1.2.1]
[]  ]
]

[7]: ObjectId: 2.5.29.37 Criticality=false
ExtendedKeyUsages [
  serverAuth
  clientAuth
]

[8]: ObjectId: 2.5.29.15 Criticality=true
KeyUsage [
  DigitalSignature
  Key_Encipherment
]

[9]: ObjectId: 2.5.29.17 Criticality=false
SubjectAlternativeName [
  DNSName: habby.mobi
  DNSName: *.habby.mobi
]

[10]: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 4C AD 52 D4 09 19 49 EC   6A DD D4 38 03 FC 58 09  L.R...I.j..8..X.
0010: 33 86 E0 CF                                        3...
]
]

]
  Algorithm: [SHA256withRSA]
  Signature:
0000: 2F FA BF 2E 50 67 35 52   9D 2A 50 F6 8F 7E 6C 7A  /...Pg5R.*P...lz
0010: B8 DA 89 5C B8 60 D2 E3   D4 E9 60 0E F9 24 62 79  ...\.`....`..$by
0020: C0 46 40 37 82 46 AD A7   CF 98 3F 99 91 7D C4 C0  .F@7.F....?.....
0030: 9B D1 A7 08 04 F8 65 96   79 06 49 40 76 56 7B 09  ......e.y.I@vV..
0040: BD 64 37 21 95 28 4D 4D   ED 39 C8 E7 FE 76 BF 94  .d7!.(MM.9...v..
0050: 52 E4 F7 8D D9 9E 34 00   99 55 9A DC 72 AA 86 47  R.....4..U..r..G
0060: 80 B9 42 FC DF 0C FB 70   C8 78 D7 64 36 08 2E 04  ..B....p.x.d6...
0070: 82 5E 35 55 5A 44 94 1C   BF 4E 20 42 AF CB 76 6F  .^5UZD...N B..vo
0080: EB B1 7D DB 42 EE 17 B7   ED 98 38 A4 94 E4 95 6B  ....B.....8....k
0090: 78 49 59 B3 13 BC 60 EC   40 86 F5 50 F9 2C 09 84  xIY...`.@..P.,..
00A0: AA DD 5C 9E B9 0F 86 4C   56 AD 8D EF 4E 88 7A A6  ..\....LV...N.z.
00B0: F6 D6 49 1C B6 34 D1 8C   10 CE C8 AB 09 D9 C5 CF  ..I..4..........
00C0: E0 40 FA 73 65 02 48 B5   AD 24 10 CE 58 EC E7 CB  .@.se.H..$..X...
00D0: 50 AB D3 26 82 9B FF A1   AA 39 7A 12 3D B3 7D 82  P..&.....9z.=...
00E0: E3 C0 01 AA 9A FB CB 17   F5 BF E4 DB A7 9C 66 A0  ..............f.
00F0: 2C 50 49 BB C2 56 E1 C9   87 90 F7 62 61 D9 1A 09  ,PI..V.....ba...

]
-----END CERTIFICATE-----
"""

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


def generate_cert():
    # Create a self-signed certificate
    cert = crypto.X509()
    cert.get_subject().CN = "habby.mobi"
    cert.set_serial_number(1000)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10*365*24*60*60)
    cert.set_issuer(cert.get_subject())
    cert.set_pubkey(pkey)
    cert.sign(pkey, 'sha256')

    # Write the certificate to a file
    with open("Certificates/cert.pem", "wb") as f:
        f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert))

    # Write the private key to a file
    with open("Certificates/key.pem", "wb") as f:
        f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, pkey))

class Client:
    def __init__(self, socket):
        self.socket = socket

    def recv(self):
        while True:
            time.sleep(0.5)
            
            try: 
                data = self.socket.recv(4096)
            except Exception as e:
                print(f'[-] Cannot recv data on socket, error: {e}')
                
            # try:
            #     data = self.socket.recv(1024).hex()
            # except Exception as e:
            #     print(f'[-]: {e}')

            if len(data) > 0:
                
                try:
                    self.port = self.socket.getsockname()[1]
                    
                    if self.port == 443:
                        print(f'[Recv (port:{self.port})]: {data}')
                        print('')
                except Exception as e:
                    print(f'[-]: Cannot find port of socket, error: {e}')
                
                #self.socket.send(data)
                                  



def onNewClient(clientSocket, clientAddress, isSSL):
    print(f'[+]: New client connected: {clientAddress}')
    
    client = Client(clientSocket)
    #GameWorldManager.instances.append(client)
    Thread(target=client.recv).start()
    #Thread(target=client.gameLoop).start()
    print(f'[+]: New game client connected: {clientAddress}')
    

def loop(socket, port, isSSL):
    print(f'[+] Server started 0.0.0.0:{port}. Waiting for connections...')
    while True:
        (clientSocket, clientAddress) = socket.accept()
        if isSSL == True:
            try:
                certificate = ssl.PEM_cert_to_DER_cert(cert_str)
                context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                context.load_cert_chain(certfile=None, keyfile=None, cert_chain=certificate)
                #context.load_cert_chain(certfile="Certificates/cert.pem", keyfile="Certificates/key.pem")
                clientSocket = context.wrap_socket(clientSocket, server_side=True)
                print(f'[+]: SSL connection established: {clientAddress}')
            except Exception as e:
                print(f'[-]: SSL connection errored: {e}')
                break
        
        onNewClient(clientSocket, clientAddress, isSSL)


if __name__ == "__main__":   

    # Kill process if running earlier
    subprocess.run(["sudo", "pkill", "python"])
    
    # Generate a private key
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)

    # Generate the certificate
    generate_cert()


    # 9952, 8080, (443)
    # 12132, 9952, 8080
    ports = []
    sockets = [
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ]

    sslPort = 443    
    sslSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslSocket.bind(("0.0.0.0", sslPort))
    sslSocket.listen(10)
    sslSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    for s in sockets:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    Thread(target=loop, args=(sslSocket, sslPort, True,)).start()
    
    for i in range(len(sockets)):
        port = ports[i]
        s = sockets[i]
        s.bind(("0.0.0.0", port))
        s.listen(10)
        Thread(target=loop, args=(s, port, False,)).start()