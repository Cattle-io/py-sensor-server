import json
from django.views.decorators.csrf import csrf_exempt
from channels.layers import get_channel_layer
import sys

from asgiref.sync import AsyncToSync
from asgiref.sync import async_to_sync

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from modules.devices.models import Device
from modules.animals.models import Animal
from modules.experiments.models import Experiment

from .models import Packet
from .models import PacketIP
from .models import PacketBasic
from .models import PacketHealth
from .models import PacketHeat
from .models import PacketIMU
from .models import PacketCH4

from .serializers import PacketsSerializer
from .serializers import PacketsHealthSerializer
from .serializers import PacketsHeatSerializer
from .serializers import PacketsIMUSerializer
from .serializers import PacketsCH4Serializer




def method_get():

    data = []

    packets = PacketBasic.objects.all()
    serializer = PacketsSerializer(packets, many=True)
    dataPackets = serializer.data

    packetsHealth = PacketHealth.objects.all()
    serializerHealth = PacketsHealthSerializer(packetsHealth, many=True)
    dataPacketsHealth = serializerHealth.data

    packetsHeat = PacketHeat.objects.all()
    serializerHeat = PacketsHeatSerializer(packetsHeat, many=True)
    dataPacketsHeat = serializerHeat.data

    packetsIMU = PacketIMU.objects.all()
    serializerIMU = PacketsIMUSerializer(packetsIMU, many=True)
    dataPacketsIMU = serializerIMU.data

    packetsCH4 = PacketCH4.objects.all()
    serializerCH4 = PacketsCH4Serializer(packetsCH4, many=True)
    dataPacketsCH4 = serializerCH4.data

    data.append(dataPacketsHealth)
    data.append(dataPacketsHeat)
    data.append(dataPacketsIMU)
    data.append(dataPacketsCH4)
    data_flatten = [val for sublist in data for val in sublist]
    data_sorted = sorted(data_flatten, key=lambda x : x['timestamp'], reverse=False)

    return Response(data_sorted, status=status.HTTP_201_CREATED)


def method_get_device_id_exp_id(request, device_id, experiment_id):

    data = []

    packets = PacketBasic.objects.filter(device_id=device_id, experiment_id=experiment_id)
    serializer = PacketsSerializer(packets, many=True)
    dataPackets = serializer.data

    packetsHealth = PacketHealth.objects.filter(device_id=device_id, experiment_id=experiment_id)
    serializerHealth = PacketsHealthSerializer(packetsHealth, many=True)
    dataPacketsHealth = serializerHealth.data

    packetsHeat = PacketHeat.objects.filter(device_id=device_id, experiment_id=experiment_id)
    serializerHeat = PacketsHeatSerializer(packetsHeat, many=True)
    dataPacketsHeat = serializerHeat.data

    packetsIMU = PacketIMU.objects.filter(device_id=device_id, experiment_id=experiment_id)
    serializerIMU = PacketsIMUSerializer(packetsIMU, many=True)
    dataPacketsIMU = serializerIMU.data

    packetsCH4 = PacketCH4.objects.filter(device_id=device_id, experiment_id=experiment_id)
    serializerCH4 = PacketsCH4Serializer(packetsCH4, many=True)
    dataPacketsCH4 = serializerCH4.data

    data.append(dataPacketsHealth)
    data.append(dataPacketsHeat)
    data.append(dataPacketsIMU)
    data.append(dataPacketsCH4)

    data_flatten = [val for sublist in data for val in sublist]
    data_sorted = sorted(data_flatten, key=lambda x : x['timestamp'], reverse=False)

    return HttpResponse(json.dumps(data_sorted), content_type='application/json')

def method_get_id(id):
    packet = Packet.objects.get(id=id)
    serializer = PacketsSerializer(packet)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
def method_post(data):
    serializer = PacketsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_patch(id, data):
    packet = Packet.objects.get(id=id)
    serializer = PacketsSerializer(packet, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_delete(id):
    serializer = PacketsSerializer.objects.get(id=id)
    if serializer.is_valid(raise_exception=True):
        serializer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def module_crud(request):
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        return method_get() 
    if request.method == 'POST':
        return method_post(request.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def module_crud_id(request, id):
    """
    List all code Books, or create a new Book.
    """
    if request.method == 'GET':
        return method_get_id(id) 
    if request.method == 'PATCH':
        return method_patch(id, request.data)
    if request.method == 'DELETE':
        return method_delete(id) 




def get_packet(device_id, animal_id, experiment_id, packet_json, packet_raw):
    packet_type = packet_json['type']
    if packet_type == 'HEALT':
        battery_percentage = packet_json.get('battery','')
        signal_percentage = packet_json.get('signal','')
        return PacketHealth(battery_percentage=battery_percentage, signal_percentage=signal_percentage, experiment_id=experiment_id,device_id=device_id,raw=packet_raw)
    elif packet_type == 'IP':
        ip_address = packet_json.get('ip','')
        return PacketIP(ip=ip_address, experiment_id=experiment_id, device_id=device_id, raw=packet_raw)
    elif packet_type == 'HEAT':
        temperature_degree = packet_json.get('temperature','')
        humidity_percentage = packet_json.get('humidity','')
        return PacketHeat(temperature_degree=temperature_degree, humidity_percentage=humidity_percentage, experiment_id=experiment_id,device_id=device_id,raw=packet_raw)
    elif packet_type == 'IMU':
        acc_x =  packet_json.get('ax','')
        acc_y =  packet_json.get('ay','')
        acc_z =  packet_json.get('az','')
        gyro_x =  packet_json.get('gx','')
        gyro_y =  packet_json.get('gy','')
        gyro_z =  packet_json.get('gz','')
        magn_x =  packet_json.get('mx','')
        magn_y =  packet_json.get('my','')
        magn_z = packet_json.get('mz','')
        bar =  packet_json.get('bar','')
        angle_psi_degree =  packet_json.get('psi','')
        angle_phi_degree =  packet_json.get('phi','')
        angle_theta_degree =  packet_json.get('theta','')
        z_mtrs =  packet_json.get('z','')
        return PacketIMU(acc_x=acc_x,acc_y=acc_y,acc_z=acc_z,gyro_x=gyro_x,gyro_y=gyro_y,gyro_z=gyro_z,magn_x=magn_x,magn_y=magn_y,magn_z=magn_z,bar=bar,angle_psi_degree=angle_psi_degree,angle_phi_degree=angle_phi_degree,angle_theta_degree=angle_theta_degree,z_mtrs=z_mtrs,experiment_id=experiment_id,device_id=device_id,raw=packet_raw)
    elif packet_type == 'CH4':
        ch4_ppm = packet_json.get('ch4_ppm','')
        ch4_adc = packet_json.get('ch4_adc','')
        print('WE ARE HERE')
        return PacketCH4(ch4_ppm=ch4_ppm, ch4_adc=ch4_adc, experiment_id=experiment_id,device_id=device_id,raw=packet_raw)
    else:
        return Packet(experiment_id=experiment_id,device_id=device_id,raw=packet_raw)


@csrf_exempt
def handle_tcp_packet(request):
    try:
        packet_raw = request.body.decode("utf-8")
        packet_json = json.loads(packet_raw)
        if('uid' in packet_json):
            packet_uid = packet_json['uid']
            device = Device.objects.first()
            if(device):
                device = Device.objects.filter(uid=packet_uid).first()
                animal = Animal.objects.filter(id=device.animal_id).first()
                experiment = Experiment.objects.filter(id=device.experiment_id).first()
                packet = get_packet(device_id=device.id, animal_id=device.animal_id, experiment_id=device.experiment_id, packet_json=packet_json, packet_raw=packet_raw)
                if(experiment.status == 'PLAY'):         
                    packet.save()
            else: 
                device = Device(animal_id=0, experiment_id=0, ip=packet_json['ip'], uid=packet_uid,name='', category='', firmware='', status='', picture_url='', last_battery_level='', last_signal_level='')
                device.save()
                packet = get_packet(device_id=device.id, animal_id=0, experiment_id=0, packet_json=packet_json, packet_raw=packet_raw)
                packet.save()

            stream_packet(packet_raw)
        else:
            print('CHAT PACKET')
            print(packet_json)
       
        return JsonResponse({'STATUS': 'OK'})
    except Exception as e:
        print(e)
        return JsonResponse({'STATUS': 'FAILED'})

def stream_packet(message):
    try:

        channel_layer = get_channel_layer()
        channel_room_name = 'stream_chat'

        print(' ')
        print('[STREAM_PACKET] @def stream_packet(message) => send to channel')
        print(' ')
    
        async_to_sync(channel_layer.group_send)(
        'chat_stream', {
            "type": "chat_message",
            "message": message,
        })

    except Exception as e:
        print(' ')
        print(' ')
        print('PAILAS PERRITO')
        print(e)
        print(' ')
        print(' ')

@csrf_exempt
def get_ch4_packets_by_experiment_id(request, experiment_id):
    data = []
    packetsCH4 = PacketCH4.objects.filter(experiment_id=experiment_id)
    serializerCH4 = PacketsCH4Serializer(packetsCH4, many=True)
    dataPacketsCH4 = serializerCH4.data
    data.append(dataPacketsCH4)
    data_flatten = [val for sublist in data for val in sublist]
    data_sorted = sorted(data_flatten, key=lambda x : x['timestamp'], reverse=False)
    return HttpResponse(json.dumps(data_sorted), content_type='application/json')

@csrf_exempt
def delete_packets_by_experiment_id(request, experiment_id):
    PacketCH4.objects.filter(experiment_id=experiment_id).delete()
    return HttpResponse(json.dumps({'status':'ok'}), content_type='application/json')
