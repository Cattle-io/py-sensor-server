from django.db import models

class UserPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    rol_id = models.IntegerField()
    email = models.URLField(max_length=200, blank=False)
    password = models.CharField(max_length=100)
    image = models.FilePathField(path="/img")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class RolPerson(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description =  models.CharField(max_length=500)
    image = models.FilePathField(path="/img")
    privileges_users = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    privileges_projects = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    privileges_devices = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    privileges_experiments = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    privileges_animals = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    privileges_reports = models.CharField(max_length=12) # ALLOW_SEE, ALLOW_EDIT, NOT_ALLOW
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
