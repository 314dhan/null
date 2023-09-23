import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Connect to the server
s.connect(server_address)

# Send data to the server
message = "Hello, server!"
s.sendall(message.encode())

# Receive data from the server
data = s.recv(1024)
print("Received:", data.decode())

# Close the socket
s.close()
