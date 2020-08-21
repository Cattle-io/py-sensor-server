from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from modules.animals.models import Animal
from modules.animals.serializers import AnimalsSerializer

def method_get():
    animals = Animal.objects.all()
    serializer = AnimalsSerializer(animals, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def method_get_id(id):
    animal = Animal.objects.get(id=id)
    serializer = AnimalsSerializer(animal)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def method_post(data):
    serializer = AnimalsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_patch(id, data):
    animal = Animal.objects.get(id=id)
    serializer = AnimalsSerializer(animal, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_delete(id):
    animal = Animal.objects.get(id=id)
    animal.delete()
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
