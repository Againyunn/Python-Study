import socket
from threading import local

from numpy import byte

localIP = "127.0.0.1"
localPort = 12345

bufferSize = 1024 #담아올 데이터의 버퍼

UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP Server Socket UP and Listening")

while(True):
    dataPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytes.decode(dataPair[0]) #데이터
    address = dataPair[1] #누가 보냈는 지

    msgFromClient = "Message From Client[{}] {}".format(address, message)

    print(msgFromClient)

    msgFromServer1 = "Welcome It's server!"

    byteToSend1 = str.encode(msgFromServer1)

    UDPServerSocket.sendto(byteToSend1, address)

    msgFromServer2 = f"{message}"

    byteToSend2 = str.encode(msgFromServer2)

    UDPServerSocket.sendto(byteToSend2, address)



