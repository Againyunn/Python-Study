import socket

msgFromClient = "Hello Computer Network"
byteToSend = str.encode(msgFromClient)
bufferSize = 1024
serverAddress = ("127.0.0.1", 12345)


UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

UDPClientSocket.sendto(byteToSend, serverAddress)

for i in range(2):
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)

    decodedMsg = bytes.decode(msgFromServer[0])

    msg = "Message from Server {}".format(decodedMsg)
    print(msg)