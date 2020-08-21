from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from modules.users.models import UserPerson
from modules.users.serializers import UsersSerializer

def method_get():
    users = UserPerson.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

def method_get_id(id):
    user = UserPerson.objects.get(id=id)
    serializer = UsersSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
    
def method_post(data):
    serializer = UsersSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(data, status=status.HTTP_201_CREATED)
    else: 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_patch(id, data):
    user = UserPerson.objects.get(id=id)
    serializer = UsersSerializer(user, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.validated_data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def method_delete(id):
    serializer = UsersSerializer(UserPerson.objects.get(id=id))
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
