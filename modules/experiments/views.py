from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from modules.experiments.models import Experiment
from modules.experiments.serializers import ExperimentsSerializer

def method_get():
    experiments = Experiment.objects.all()
    serializer = ExperimentsSerializer(experiments, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def method_get_id(id):
    animal = Experiment.objects.get(id=id)
    serializer = ExperimentsSerializer(animal)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def method_post(data):
    serializer = ExperimentsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_patch(id, data):
    experiment = Experiment.objects.get(id=id)
    serializer = ExperimentsSerializer(experiment, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_delete(id):
    experiment = Experiment.objects.get(id=id)
    experiment.delete()
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
def do_play_by_id(request, experiment_id):
    data = { 'status' : 'PLAY' }
    experiment = Experiment.objects.get(id=experiment_id)
    serializer = ExperimentsSerializer(experiment, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def do_pause_by_id(request, experiment_id):
    data = { 'status' : 'PAUSE' }
    experiment = Experiment.objects.get(id=experiment_id)
    serializer = ExperimentsSerializer(experiment, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return JsonResponse(data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

