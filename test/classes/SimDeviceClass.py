import json
import asyncio
import websockets
import random
import time
import socket
from random import randrange

from faker import Faker
faker = Faker()

CATTLE_IO_SERVER_HOST = '192.168.1.245'
CATTLE_IO_SERVER_PORT = 9003


class Device:
    def __init__(self, uid):

        self.uid = uid
        self.ip = faker.ipv4()
        self.battery = 100.00
        self.signal = 100.00
        self.temperature = 34.00 - 0.025 * random.randrange(
            50, 100) + 0.025 * random.randrange(50, 100)
        self.humidity = 70.00 - 0.005 * random.randrange(
            1000, 2000) + 0.005 * random.randrange(1000, 2000)
        self.ax = 7.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.ay = 0.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.az = -10.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gx = 7.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gy = 0.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gz = 1.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.mx = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.my = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.mz = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.ch4 = 100 + 0.025 * random.randrange(
            2000, 5000) - 0.025 * random.randrange(2000, 5000)
        self.batteryStr = '{0:.2f}'.format(self.temperature)
        self.signalStr = '{0:.2f}'.format(self.humidity)
        self.temperatureStr = '{0:.2f}'.format(self.temperature)
        self.humidityStr = '{0:.2f}'.format(self.humidity)
        self.axStr = '{0:.2f}'.format(self.ax)
        self.ayStr = '{0:.2f}'.format(self.ay)
        self.azStr = '{0:.2f}'.format(self.az)
        self.gxStr = '{0:.2f}'.format(self.gx)
        self.gyStr = '{0:.2f}'.format(self.gy)
        self.gzStr = '{0:.2f}'.format(self.gz)
        self.mxStr = '{0:.2f}'.format(self.mx)
        self.myStr = '{0:.2f}'.format(self.my)
        self.mzStr = '{0:.2f}'.format(self.mz)
        self.ch4Str = '{0:.2f}'.format(self.ch4)

    def connect(self):
        # create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect the client
        # client.connect((target, port))
        self.client.connect((CATTLE_IO_SERVER_HOST, CATTLE_IO_SERVER_PORT))

    def send_packet_ip(self):
        print(' \n >> SENDING IP PACKET ')
        message = '{ "uid":"' + self.uid + '", "type":"IP", "ip": "' + self.uid + '" , "message":"DEVICE OK!" }'
        self.client.send(message.encode('utf-8'))
        time.sleep(0.5)
        self.client.close()

    def send_packet_health(self):
        print(' \n >> SENDING HEALTH PACKET ')
        message = '{ "uid":"' + self.uid + '", "type":"HEALT", "battery": "' + self.batteryStr + '", "signal": "' + self.signalStr + '" }'
        self.client.send(message.encode('utf-8'))
        response = self.client.recv(4096)
        self.client.close()

    def send_packet_heat(self):
        print(' \n >> SENDING HEAT PACKET ')
        message = '{ "uid":"' + self.uid + '", "type":"HEAT", "temperature": "'+self.temperatureStr+'", "humidity": "'+self.humidityStr+'" }'
        self.client.send(message.encode('utf-8'))
        response = self.client.recv(4096)
        self.client.close()

    def send_packet_imu(self):
        print(' \n  >> SENDING HEAT PACKET ')
        message = '{ "uid":"' + self.uid + '", "type":"IMU", "ax":"'+self.axStr+'", "ay":"'+self.ayStr+'", "az": "'+self.azStr+'" }'
        self.client.send(message.encode('utf-8'))
        response = self.client.recv(4096)
        self.client.close()

    def send_packet_ch4(self):
        print(' \n  >> SENDING CH4 PACKET ')
        message = '{ "uid":"' + self.uid + '", "type":"CH4", "ch4_ppm":"'+self.ch4Str+'", "ch4_adc":"'+self.ch4Str+'" }'
        self.client.send(message.encode('utf-8'))
        response = self.client.recv(4096)
        self.client.close()

    def do_measure(self):
        self.battery = max(0, self.battery - 1)
        self.signal = 80 + random.randint(0,20)
        self.temperature = 34.00 - 0.025 * random.randrange(
            50, 100) + 0.025 * random.randrange(50, 100)
        self.humidity = 70.00 - 0.005 * random.randrange(
            1000, 2000) + 0.005 * random.randrange(1000, 2000)
        self.ax = 7.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.ay = 0.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.az = -10.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gx = 7.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gy = 0.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.gz = 1.16000 + 0.005 * random.randrange(
            1000, 2000) - 0.005 * random.randrange(1000, 2000)
        self.mx = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.my = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.mz = 0.16000 + 0.0025 * random.randrange(
            2000, 5000) - 0.0025 * random.randrange(2000, 5000)
        self.ch4 = 100 + 0.025 * random.randrange(
            2000, 5000) - 0.025 * random.randrange(2000, 5000)
        self.batteryStr = '{0:.2f}'.format(self.battery)
        self.signalStr = '{0:.2f}'.format(self.signal)
        self.temperatureStr = '{0:.2f}'.format(self.temperature)
        self.humidityStr = '{0:.2f}'.format(self.humidity)
        self.axStr = '{0:.2f}'.format(self.ax)
        self.ayStr = '{0:.2f}'.format(self.ay)
        self.azStr = '{0:.2f}'.format(self.az)
        self.gxStr = '{0:.2f}'.format(self.gx)
        self.gyStr = '{0:.2f}'.format(self.gy)
        self.gzStr = '{0:.2f}'.format(self.gz)
        self.mxStr = '{0:.2f}'.format(self.mx)
        self.myStr = '{0:.2f}'.format(self.my)
        self.mzStr = '{0:.2f}'.format(self.mz)
        self.ch4Str = '{0:.2f}'.format(self.ch4)