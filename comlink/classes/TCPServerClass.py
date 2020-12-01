'''
import socket
import threading
import json
import asyncio
import requests

class ServerTCP:

    def __init__(self, ip, port):
    
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server.bind((ip, port))
        print('TCP Server Listening on {}:{}'.format(ip, port))

        while True:
                lock.acquire()
                data, addr = s.recvfrom(1024)
                data = data.decode()
                print(' DATOS DEL NODEMCU ')
                print(data)

    def handle_client_connection(self, client_socket):
            request = client_socket.recvfrom(1024)
            data = request.decode()
            print('data ')
            print(data)
            print(' ')
            #self.handle_packet(request)

    def start(self):
        while True:
            client_sock, address = self.server.accept()
            print('Accepted connection from {}:{}'.format(address[0], address[1]))
            client_handler = threading.Thread(
                target=self.handle_client_connection,
                args=(client_sock,)
            )
            client_handler.daemon = True
            client_handler.start()

    def handle_packet(self, raw):
        try:
            http_url = 'http://localhost:8000/packets/handle_tcp_packet'
            http_payload = raw.decode("utf-8")
            http_response = requests.post(http_url, data = http_payload)
            print('http_response')
            print(http_response)
        except:
            print("[COMLINK] [TCP] FAILED SAVING IN DJANGO SERVER ")
  
'''