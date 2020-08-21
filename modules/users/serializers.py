from rest_framework import serializers
from modules.users.models import UserPerson

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPerson
        fields = ('id', 'name', 'rol_id','email','password','image','created_at','updated_at')
