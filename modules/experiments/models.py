from django.db import models

class Experiment(models.Model):

    id = models.AutoField(primary_key=True)
    project_id = models.IntegerField()
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    duration_hrs = models.FloatField(default=0.000)
    started_at = models.DateTimeField(null=True, blank=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
