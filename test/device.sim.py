#!/usr/bin/env python
import json
import asyncio
import websockets
import random
import time
from faker import Faker  

faker = Faker()

async def main(uri):
    while True:
        time.sleep(5)
        async with websockets.connect(uri) as websocket:
            print('LOOP')

            ip = faker.ipv4()

            battery = 100.00
            signal = 100.00

            temperature = 34.00 - 0.025*random.randrange(50, 100) + 0.025*random.randrange(50, 100)
            humidity = 70.00 - 0.005*random.randrange(1000, 2000) + 0.005*random.randrange(1000, 2000)

            ax = 7.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)
            ay = 0.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)
            az = -10.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)

            gx = 7.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)
            gy = 0.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)
            gz = 1.16000 + 0.005*random.randrange(1000, 2000) - 0.005*random.randrange(1000, 2000)

            mx = 0.16000 + 0.0025*random.randrange(2000, 5000) - 0.0025*random.randrange(2000, 5000)
            my = 0.16000 + 0.0025*random.randrange(2000, 5000) - 0.0025*random.randrange(2000, 5000)
            mz = 0.16000 + 0.0025*random.randrange(2000, 5000) - 0.0025*random.randrange(2000, 5000)

            ch4 = 100 + 0.025*random.randrange(2000, 5000) - 0.025*random.randrange(2000, 5000)

            batteryStr = '{0:.2f}'.format(temperature)
            signalStr = '{0:.2f}'.format(humidity)

            temperatureStr = '{0:.2f}'.format(temperature)
            humidityStr = '{0:.2f}'.format(humidity)

            axStr = '{0:.2f}'.format(ax)
            ayStr = '{0:.2f}'.format(ay)
            azStr = '{0:.2f}'.format(az)

            gxStr = '{0:.2f}'.format(gx)
            gyStr = '{0:.2f}'.format(gy)
            gzStr = '{0:.2f}'.format(gz)

            mxStr = '{0:.2f}'.format(mx)
            myStr = '{0:.2f}'.format(my)
            mzStr = '{0:.2f}'.format(mz)

            ch4Str = '{0:.2f}'.format(ch4)

            await websocket.send('{ "uid":"900", "type":"IP", "ip": "'+ip+'" , "message":"OY HEAR!" }')
            await websocket.send('{ "uid":"901", "type":"HEALT", "battery": "'+batteryStr+'", "signal": "'+signalStr+'" }')
            await websocket.send('{ "uid":"901", "type":"HEAT", "temperature": "'+temperatureStr+'", "humidity": "'+humidityStr+'" }')
            await websocket.send('{ "uid":"901", "type":"IMU", "ax":"'+axStr+'", "ay":"'+ayStr+'", "az": "'+azStr+'" }')
            await websocket.send('{ "uid":"901", "type":"CH4", "ch4":"'+ch4Str+'" }')
            #await websocket.recv()

        
loop = asyncio.get_event_loop()
loop.run_until_complete(main('ws://127.0.0.1:8000/ws/sockets/900/'))
loop.close()

    
    