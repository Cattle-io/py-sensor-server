import socket
import threading
import json
import asyncio
import requests
import sys
import os

localIP     = "192.168.0.13"
localPort   = 9205

bufferSize  = 1024

def handle_packet(raw):
    try:

        print('[COMLINK] [PACKET] message')
        print(raw)

        http_url = 'http://localhost:8000/packets/handle_tcp_packet'
        http_payload = raw.decode("utf-8")
        http_response = requests.post(http_url, data = http_payload)

    except:
        print("[COMLINK] [TCP] FAILED SAVING IN DJANGO SERVER ")

def main():

    # Create a datagram socket
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    UDPServerSocket.bind((localIP, localPort))

    # Listen for incoming datagrams
    while(True):

        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        handle_packet(message)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)