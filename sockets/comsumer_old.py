import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from modules.animals.models import Animal
from modules.devices.models import Device
from modules.packets.views import get_packet

class SocketConsumer(WebsocketConsumer):
    
    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'device_%s' % self.room_name

        print('room_name')
        print(self.room_name)


        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):

        raw = text_data
        packet_json = json.loads(raw)

        if('uid' in packet_json):
            packet_uid = packet_json['uid']
            device = Device.objects.filter(uid=packet_uid).first()

            if(device):

                device = Device.objects.filter(uid=packet_uid).first()
                animal = Animal.objects.filter(id=device.animal_id).first()

                packet = get_packet(device_id=device.id, animal_id=device.animal_id, experiment_id=device.experiment_id, packet_json=packet_json, packet_raw=raw)
                packet.save()

            else:
                
                device = Device(animal_id=0,experiment_id=0,ip=packet_json['ip'],uid=packet_uid,name='',category='',firmware='',status='',picture_url='',last_battery_level='',last_signal_level='')
                device.save()

                packet = get_packet(device_id=device.id, animal_id=0, experiment_id=0, packet_json=packet_json, packet_raw=raw)
                packet.save()
                
        else:
            # Send message to room group
            print('CHAT PACKET')
            print(raw)
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            self.send(text_data=json.dumps({
                'message': message
            }))


    def send_packet_to_angular(self,event):
        
            print(" ")
            print(" > EVENT TRIGERED")
            print(" ")

            # Receive message from room group
            message = event['message']
            # Send message to WebSocket
            self.send(text_data=json.dumps({
                'message': message
            }))