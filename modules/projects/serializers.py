from rest_framework import serializers
from modules.projects.models import Project

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title','image','description','department','city','place_name','place_category','place_lat','place_lng','created_at','updated_at')
