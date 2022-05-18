import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    data = input("SEND( type q or Q to Quit :")
    client_socket.send(data.encode())
    
    if data == 'q' or data == 'Q':
        client_socket.close()
        break

print("socket closed")