from django.db import models

class Packet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10, default='DEFAULT')
    device_id = models.IntegerField()
    experiment_id = models.IntegerField()
    raw = models.CharField(max_length=200, default=' ')
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class PacketBasic(Packet):
    name = 'OTHER'
    property_1 = models.CharField(max_length=200, default=' ')

class PacketIP(Packet):
    name = 'IP'
    ip = models.CharField(max_length=12, default=' ')
    uid = models.CharField(max_length=12, default=' ')

class PacketHealth(Packet):
    name = 'HEALTH'
    battery_percentage = models.CharField(max_length=200, default=' ')
    signal_percentage = models.CharField(max_length=200, default=' ')
    
class PacketHeat(Packet):
    name = 'HEAT'
    temperature_degree = models.CharField(max_length=200, default=' ')
    humidity_percentage = models.CharField(max_length=200, default=' ')

class PacketIMU(Packet):
    name = 'IMU'
    acc_x = models.CharField(max_length=200, default=' ')
    acc_y = models.CharField(max_length=200, default=' ')
    acc_z = models.CharField(max_length=200, default=' ')
    gyro_x = models.CharField(max_length=200, default=' ')
    gyro_y = models.CharField(max_length=200, default=' ')
    gyro_z = models.CharField(max_length=200, default=' ')
    magn_x = models.CharField(max_length=200, default=' ')
    magn_y = models.CharField(max_length=200, default=' ')
    magn_z = models.CharField(max_length=200, default=' ')
    bar = models.CharField(max_length=200, default=' ')
    angle_psi_degree = models.CharField(max_length=200, default=' ')
    angle_phi_degree = models.CharField(max_length=200, default=' ')
    angle_theta_degree = models.CharField(max_length=200, default=' ')
    z_mtrs = models.CharField(max_length=200, default=' ')

class PacketCH4(Packet):
    name = 'CH4'
    ch4_ppm = models.CharField(max_length=200, default=' ')


