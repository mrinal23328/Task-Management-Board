from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_updation = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')


