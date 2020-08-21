import json

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from modules.packets.models import Packet
from modules.packets.models import PacketIP
from modules.packets.models import PacketBasic
from modules.packets.models import PacketHealth
from modules.packets.models import PacketHeat
from modules.packets.models import PacketIMU
from modules.packets.models import PacketCH4

from modules.packets.serializers import PacketsSerializer
from modules.packets.serializers import PacketsHealthSerializer
from modules.packets.serializers import PacketsHeatSerializer
from modules.packets.serializers import PacketsIMUSerializer
from modules.packets.serializers import PacketsCH4Serializer




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
        ch4_ppm = packet_json.get('ch4','')
        return PacketCH4(ch4_ppm=ch4_ppm, experiment_id=experiment_id,device_id=device_id,raw=packet_raw)
    else:
        return Packet(experiment_id=experiment_id,device_id=device_id,raw=packet_raw)