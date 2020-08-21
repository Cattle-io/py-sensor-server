from django.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    animal_id = models.IntegerField(default=0)
    experiment_id = models.IntegerField(default=0)
    ip = models.CharField(max_length=50)
    uid = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=600)
    firmware = models.CharField(max_length=5) 
    status = models.CharField(max_length=200)
    picture_url = models.CharField(max_length=2000, blank=True)
    last_signal_level = models.CharField(max_length=6) 
    last_battery_level = models.CharField(max_length=6) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)