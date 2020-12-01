#!/usr/bin/env python
import sys	#for exit
import json
import asyncio
import websockets
import random
import time

from classes.SimDeviceClass import Device

dev901 = Device('901')

dev901.connect()
dev901.send_packet_ip()
time.sleep(5)

# Main Loop in NodeMCU
dev901.do_measure()

dev901.connect()
dev901.send_packet_ch4()
time.sleep(1)

dev901.connect()
dev901.send_packet_ch4()
time.sleep(1)

dev901.connect()
dev901.send_packet_ch4()
time.sleep(1)

for i in range(2660):
    dev901.do_measure()
    dev901.connect()
    dev901.send_packet_ch4()
    time.sleep(1)



sys.exit()