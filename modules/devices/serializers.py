from rest_framework import serializers
from modules.devices.models import Device

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'animal_id', 'experiment_id', 'ip', 'uid', 'name', 'category', 'firmware', 'status','picture_url','last_signal_level','last_battery_level', 'created_at','updated_at')
