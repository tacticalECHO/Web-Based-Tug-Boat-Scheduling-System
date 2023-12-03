from django.db import models

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)

def __str__(self):
    return self.name

def __str__(self):
    return self.email

def __str__(self):
    return self.id