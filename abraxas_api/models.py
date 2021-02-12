from django.db import models

class Task(models.Model):
    task_id = models.IntegerField()
    description = models.CharField(max_length=255)
    duration = models.IntegerField()
    status = models.CharField(default='pendiente', max_length=10)
    timespan = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
