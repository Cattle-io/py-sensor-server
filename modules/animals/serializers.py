from rest_framework import serializers
from modules.animals.models import Animal

class AnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('id', 'name', 'breed', 'age', 'weight', 'picture_url', 'created_at','updated_at')
