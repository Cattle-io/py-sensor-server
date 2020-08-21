from rest_framework import serializers
from modules.packets.models import Packet
from modules.packets.models import PacketIP
from modules.packets.models import PacketHealth
from modules.packets.models import PacketHeat
from modules.packets.models import PacketIMU
from modules.packets.models import PacketCH4


class PacketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = ('id', 'name', 'raw', 'experiment_id', 'device_id',
                  'timestamp')


class PacketsHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketHealth
        fields = ('id', 'name', 'raw', 'battery_percentage',
                  'signal_percentage', 'experiment_id', 'device_id',
                  'timestamp')


class PacketIPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketIP
        fields = ('id', 'name', 'raw', 'uid', 'timestamp')


class PacketsHeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketHeat
        fields = ('id', 'name', 'temperature_degree', 'humidity_percentage',
                  'raw', 'experiment_id', 'device_id', 'timestamp')


class PacketsIMUSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketIMU
        fields = ('id', 'name', 'raw', 'experiment_id', 'device_id',
                  'timestamp', 'acc_x', 'acc_y', 'acc_z', 'gyro_x', 'gyro_y',
                  'gyro_z', 'magn_x', 'magn_y', 'magn_z', 'bar',
                  'angle_psi_degree', 'angle_phi_degree', 'angle_theta_degree',
                  'z_mtrs')


class PacketsCH4Serializer(serializers.ModelSerializer):
    class Meta:
        model = PacketCH4
        fields = ('id', 'name', 'ch4_ppm', 'raw', 'experiment_id', 'device_id',
                  'timestamp')
