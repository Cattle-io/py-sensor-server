import socket

import time
 

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("192.168.0.13", 9205)
bufferSize          = 1024

 

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket
while True:
    UDPClientSocket.sendto(str.encode("{ ""uid"" : ""901"" }"), serverAddressPort)
    time.sleep(2.4)
    #msgFromServer = UDPClientSocket.recvfrom(bufferSize)


    
   