from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.FilePathField(path="/img")
    description = models.CharField(max_length=500)
    department = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    place_name = models.CharField(max_length=200)
    place_category = models.CharField(max_length=200)
    place_lat = models.CharField(max_length=200)
    place_lng = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)