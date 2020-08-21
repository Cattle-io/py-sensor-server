from rest_framework import serializers
from modules.experiments.models import Experiment

class ExperimentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ('id', 'project_id', 'title', 'description','duration_hrs','started_at','finished_at', 'created_at','updated_at')
