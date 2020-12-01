from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import json
from asgiref.sync import async_to_sync

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from modules.devices.models import Device
from modules.devices.serializers import DevicesSerializer

import channels.layers


def method_get():
    devices = Device.objects.all()
    serializer = DevicesSerializer(devices, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def method_get_id(id):
    device = Device.objects.get(id=id)
    serializer = DevicesSerializer(device)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


def method_post(data):
    serializer = DevicesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def method_patch(id, data):
    device = Device.objects.get(id=id)
    serializer = DevicesSerializer(device, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def method_delete(id):
    device = Device.objects.get(id=id)
    device.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


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


@csrf_exempt
def send_command_to_device(request, uid, command):
    try:
        content = {'status': 'OK'}
        message = {}
        channel_layer = channels.layers.get_channel_layer()
        async_to_sync(channel_layer.send)('900', {'type': 'hello'})
        return HttpResponse(json.dumps(content),
                            content_type='application/json')
    except:
        content = {'status': 'ERROR'}
        return HttpResponse(json.dumps(content),
                            content_type='application/json')
