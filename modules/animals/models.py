from django.db import models

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    breed = models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=3, blank=True)
    weight = models.CharField(max_length=6, blank=True)
    picture_url = models.CharField(max_length=2000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AnimalState(models.Model):
    id = models.AutoField(primary_key=True)
    animal_id = models.IntegerField()
    experiment_id: models.IntegerField()
    state_type: models.CharField(max_length=25)
    state_started_at: models.DateTimeField(auto_now_add=True)
    state_finished_at: models.DateTimeField(auto_now_add=True)
    state_duration_minutes: models.CharField(max_length=6)
    state_accuracy_percentage: models.CharField(max_length=6)
    