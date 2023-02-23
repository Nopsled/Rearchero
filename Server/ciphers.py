# Example Python program that creates an SSLContext

# which is used to create an SSLSocket

import socket

import ssl

import os

import certifi


# Create an SSLContext instance by specifying the highest TLS protocol

# that both the client and the server supports

sslSettings = ssl.SSLContext(ssl.PROTOCOL_TLS)

sslSettings.verify_mode = ssl.CERT_REQUIRED


# Load the CA certificates used for validating the peer's certificate

sslSettings.load_verify_locations(cafile=os.path.relpath(certifi.where()),

                                  capath=None,

                                  cadata=None)


# Create a connection oriented socket

con_socket = socket.socket()


# Make SSLSocket from the connection oriented socket

sslSocket = sslSettings.wrap_socket(con_socket)

con_socket.close()


# Connect to a server using TLS

sslSocket.connect(("0.0.0.0", 443))


print("SSLContext object:")

print(sslSettings)


# Get the context from SSLSocket and print

print("SSLContext object obtained from SSLSocket:")

context = sslSocket.context

print(context)


print("The type of the secure socket created:")

print(sslSocket.context.sslsocket_class)


print("Maximum version of the TLS:")

print(sslSocket.context.maximum_version)


print("Minimum version of the TLS:")

print(sslSocket.context.minimum_version)


print("SSL options enabled in the context object:")

print(sslSocket.context.options)


print("Protocol set in the context:")

print(sslSocket.context.protocol)


print("Verify flags for certificates:")

print(sslSocket.context.verify_flags)


print("Verification mode(how to validate peer's certificate and handle failures if any):")

print(sslSocket.context.verify_mode)


# Do SSL shutdown handshake

sslSocket.unwrap()


# Close the SSLSocket instance

sslSocket.close()
