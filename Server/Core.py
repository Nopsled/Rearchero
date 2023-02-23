#!/usr/bin/env python
# sudo nodemon - -exec python Core.py
import random
import socket
import msgpack
from threading import Thread
import time
import ssl
import OpenSSL
import json
import re
import urllib.parse
import base64
import subprocess
from OpenSSL import crypto

import Config


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
class PlayerObject:
    def __init__(self, socket, id=1, y=0, x=0, angle=0.0, usingItemID=1, unk2=0, unk3=0, unk4=None, clanLeader=0, skin=0, usingAccessoryID=0, showSkull=0, unk9=0):
        pass



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



class NetUtility:

    @staticmethod
    def parse_data(data):
        pass
        # request_line, headers = data.split('\n', 1)
        # method, path, protocol = request_line.split()

        # parsed_path = urllib.parse.urlparse(path)
        # query_params = urllib.parse.parse_qs(parsed_path.query)

        # store = query_params['store'][0]
        # app_language = query_params['appLanguage'][0]
        # system_language = query_params['systemLanguage'][0]
        # app_version = query_params['appVersion'][0]
        # device_model = query_params['deviceModel'][0]

        # custom_data = query_params['customData'][0]
        # custom_data_dict = json.loads(urllib.parse.unquote(custom_data))

        # sdk_version = headers.split("\n")[0].split(":")[1].strip()
        # client_data_str = headers.split("\n")[1].split(":")[1].strip()
        # #client_data = json.loads(client_data_str)
        # content_type = headers.split("\n")[2].split(":")[1].strip()
        # if_none_match = headers.split("\n")[3].split(":")[1].strip()
        # host = headers.split("\n")[4].split(":")[1].strip()
        # accept_encoding = headers.split("\n")[5].split(":")[1].strip()
        # connection = headers.split("\n")[6].split(":")[1].strip()
        # keep_alive = headers.split("\n")[7].split(":")[1].strip()
        # te = headers.split("\n")[8].split(":")[1].strip()
        # user_agent = headers.split("\n")[9]
        
        # print(f'[-] SDK Version: {sdk_version}')
        # #print(f'[-] Client Data: {client_data}')
        # print(f'[-] Content Type: {content_type}')
        # print(f'[-] If None Match: {if_none_match}')
        # print(f'[-] Host: {host}')
        # print(f'[-] Accept Encoding: {accept_encoding}')
        # print(f'[-] Connection: {connection}')
        # print(f'[-] Keep Alive: {keep_alive}')
        # print(f'[-] TE: {te}')
        # print(f'[-] User Agent: {user_agent}')
        # print(f'[-] Store: {store}')
        # print(f'[-] App Language: {app_language}')
        # print(f'[-] System Language: {system_language}')
        # print(f'[-] App Version: {app_version}')
        # print(f'[-] Device Model: {device_model}')
        # print(f'[-] Custom Data: {custom_data}')
        # print(f'[-] Custom Data Dict: {custom_data_dict}')
        # print('')
        # print('')

    

# Reversed API of Archero.
class API:

    @staticmethod
    def users_x_announcements (request):
        pass

    # Handle requests to: /users/156815953/announcements
    @staticmethod
    def users_x_announcements (request):
        pass
    
    
        


class Client:
    def __init__(self, socket):
        self.socket = socket
        self.port = -0


    def recv(self):
        while True:
            time.sleep(0.5)
            
            try: 
                rawData = self.socket.recv(4096)
            except Exception as e:
                print(f'[-] Cannot recv data on socket, error: {e}')

            if len(rawData) > 0:
                print(rawData)
                self.socket.send(rawData)
                decodedData = rawData.decode()
                strippedData = decodedData.strip()
                #print(f'[Recv (port:{self.port}]: {decodedData}')
                

                # Split the data into the request and headers
                data2 = urllib.parse.parse_qs(strippedData)
                print(data2)
                print("")

                for endpoint in endpoints:
                    if endpoint in decodedData:
                        print(f"[+] Client requested: {endpoint}, response sent back to client.")
                        #response = Config.Header.RESPONSE_HEADER + endpoints[endpoint]
                        #self.socket.send(response)
                        #print(response)
                        break
                    
                # if "data/config/MazeConfig.json" in decodedData:
                #     response = Config.Header.RESPONSE_HEADER + Config.GameConfig.RESPONSE
                #     print("[+] Client requested: data/config/game_config.json, response sent back to client.")
                #     self.socket.send(response)
                #     print(response)
                # elif "data/config/pvp_reward.json" in decodedData:
                #     response = Config.Header.RESPONSE_HEADER + Config.GameConfig.RESPONSE
                #     print("[+] Client requested: data/config/game_config.json, response sent back to client.")
                #     self.socket.send(response)
                #     print(response)
                # elif 



                if re.search(r"users/\d+/announcements", decodedData):
                    response = b"""HTTP/1.1 304 Not Modified
                    Connection: close
                    Vary: Accept-Encoding
                    Date: Mon, 20 Feb 2023 19:17:23 GMT
                    X-Powered-By: Express
                    ETag: W/"1d-qTxd3JymBGkwYt6o0i73c1lZiUA"
                    X-Cache: Miss from cloudfront
                    Via: 1.1 648da69bb4c2221c403be08a06311d98.cloudfront.net (CloudFront)
                    X-Amz-Cf-Pop: ARN56-P1
                    X-Amz-Cf-Id: YSLMFVKf-ZDsrj_ZRkCdupmcUJyeqrh3HdcMryFo8vZIw_mx7frGNQ==\r\n\r\n"""
                    self.socket.send(response)
                    print("[+] API request: users/<id>/announcements, response sent back to client.")
                    print(response)
                    print("")

                #POST /v1/projects/archero-10b8d/installations HTTP/1.1
                if "v1/projects/archero-10b8d/installations" in decodedData:
                    response = b'''HTTP/2 200 OK
                    Content-Type: application/json; charset=UTF-8
                    Vary: Origin
                    Vary: X-Origin
                    Vary: Referer
                    Date: Mon, 20 Feb 2023 23:29:37 GMT
                    Server: ESF
                    Cache-Control: private
                    Content-Length: 630
                    X-Xss-Protection: 0
                    X-Frame-Options: SAMEORIGIN
                    X-Content-Type-Options: nosniff
                    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

                    {
                    "name": "projects/828268901162/installations/cxQTspArQ2m_Dl6OsvUfaF",
                    "fid": "cxQTspArQ2m_Dl6OsvUfaF",
                    "refreshToken": "3_AS3qfwJGYt8Al5oYk5R5GrOH5A_iVW4rDi-bTk28SYxQFGJL0jzjUIJ-pG_dYfqsd-2KAZxg03a2rI7o5BGyRYb5PsgDRkbBuBf-qUSSz1TwgJc",
                    "authToken": {
                        "token": "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IjE6ODI4MjY4OTAxMTYyOmFuZHJvaWQ6NzliODUyN2ViYzA1M2M2ODhiZTQ1MyIsImV4cCI6MTY3NzU0MDU3NywiZmlkIjoiY3hRVHNwQXJRMm1fRGw2T3N2VWZhRiIsInByb2plY3ROdW1iZXIiOjgyODI2ODkwMTE2Mn0.AB2LPV8wRQIhAOXLJ5-FXc0Vvj7qtFgSLcKLdAthMYPnhvGGpFJ4kibzAiBSd41HdzooTpUzpXK1C0XoY3c13Uw82ZJCDOc4Mhlv2Q",
                        "expiresIn": "604800s"
                    }
                    }'''
                    self.socket.send(response)
                    print("[+] API request: POST / v1/projects/archero-10b8d/installations")
                    print("[+] Response: " + response.decode())

                # GET / spi/v2/platforms/android/gmp/1: 828268901162: android: 79b8527ebc053c688be453/settings?instance = 7a16ca6d37f5b937c1687f86d66188f136bb999b & build_version = 1266 & display_version = 4.9.0 & source = 4
                if "/spi/v2/platforms/android/gmp/" in decodedData:
                    response = '''HTTP/2 200 OK
                    Content-Type: application/json; charset=utf-8
                    X-Content-Type-Options: nosniff
                    Cache-Control: no-cache, no-store, max-age=0, must-revalidate
                    Pragma: no-cache
                    Expires: Mon, 01 Jan 1990 00:00:00 GMT
                    Date: Mon, 20 Feb 2023 23:29:37 GMT
                    Cross-Origin-Opener-Policy: same-origin-allow-popups
                    Server: ESF
                    X-Xss-Protection: 0
                    X-Frame-Options: SAMEORIGIN
                    Alt-Svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

                    {"settings_version":3,"cache_duration":86400,"features":{"collect_logged_exceptions":true,"collect_reports":true,"collect_analytics":false,"prompt_enabled":false,"push_enabled":false,"firebase_crashlytics_enabled":false,"collect_anrs":true,"collect_metric_kit":false,"collect_build_ids":false},"app":{"status":"activated","update_required":false,"report_upload_variant":2,"native_report_upload_variant":2},"fabric":{"org_id":"628d0027632d9c0d02e2b976","bundle_id":"com.habby.archero"},"on_demand_upload_rate_per_minute":10.0,"on_demand_backoff_base":1.2,"on_demand_backoff_step_duration_seconds":60,"app_quality":{"sessions_enabled":true,"sampling_rate":1.0,"session_timeout_seconds":1800}}'''
                    self.socket.send(response)
                    print(
                        "[+] API request: /sync, responded back to client.")
                    print("[+] Response: " + response.decode())

                # POST /sync HTTP/1.1 (receiver.habby.mobi)
                if "sync" in decodedData:
                    response = b'''HTTP/2 200 OK
                    Date: Mon, 20 Feb 2023 23:05:15 GMT
                    Content-Type: application/json;charset=utf-8
                    Content-Length: 10

                    {"code":0}\r\n\r\n'''
                    self.socket.send(response)
                    print("[+] API request: POST /sync (receiver.habby.mobi)")
                    print("[+] Response: " + response.decode())
                
                if "config?appid" in decodedData:
                    response = b'''HTTP/2 200 OK
                    Date: Mon, 20 Feb 2023 23:19:00 GMT
                    Content-Type: application/json;charset=utf-8
                    Content-Length: 69

                    {"code":0,"data":{"sync_batch_size":100,"sync_interval":60},"msg":""}\r\n\r\n'''
                    self.socket.send(response)
                    print(
                        "[+] API request: /config?appid=xxxxx, responded back to client.")
                    print("[+] Response: " + response.decode())
                
                if "session" in decodedData:
                    response = b'''HTTP/1.1 200 OK
                    content-type: application/json; charset=utf-8
                    date: Mon, 20 Feb 2023 23:29:42 GMT
                    content-length: 84
                    strict-transport-security: max-age=31536000; includeSubDomains; preload
                    x-frame-options: SAMEORIGIN
                    x-content-type-options: nosniff
                    x-robots-tag: noindex
                    connection: close

                    {"app_token":"be40xoovkp34","adid":"2e923d233df94bf905a4000937265a52","ask_in":5000}'''
                    self.socket.send(response)
                    print(
                        "[+] API request: POST app.adjust.com/session")
                    print("[+] Response: " + response.decode())


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
        (client_socket, client_address) = socket.accept()
        if isSSL == True:
            try:
                context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
                context.load_cert_chain(certfile="Certificates/cert.pem", keyfile="Certificates/key.pem")
                client_socket = context.wrap_socket(client_socket, server_side=True)
                print(f'[+] SSL connection established: {client_address}')
            except Exception as e:
                print(f'[-] SSL connection errored: {e}')
                break
        else:
            print(
                f'[+] Connection established to no SSL socket: {client_address}')
        
        onNewClient(client_socket, client_address, isSSL)


if __name__ == "__main__":   

    # Kill process if running earlier
    subprocess.run(["sudo", "pkill", "python"])



    # 12132, 9952, 8080, (443)
    ports = [443]
    sockets = [
        socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM),
        # socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ]

    # Generate a private key
    pkey = crypto.PKey()
    pkey.generate_key(crypto.TYPE_RSA, 2048)
    generate_cert()
    
    # Load the Burp Suite-generated certificate
    #with open('Certificates/burp_cert.crt', 'rb') as f:
    #    cert_data = f.read()
    #context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    #context.load_cert_chain('Certificates/burp_cert.crt')
    
    
    sslPort = 443
    sslSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sslSocket.bind(("0.0.0.0", sslPort))
    sslSocket.listen(10)
    sslSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Thread(target=loop, args=(sslSocket, sslPort, True,)).start()
    
    #for s in sockets:
    #    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # for i in range(len(sockets)):
    #     port = ports[i]
    #     s = sockets[i]
    #     s.bind(("0.0.0.0", port))
    #     s.listen(10)
    #     Thread(target=loop, args=(s, port, True,)).start()