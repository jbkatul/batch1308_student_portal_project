from django.db import models

class Registrations(models.Model):
    username = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False)
    pass1 = models.CharField(null=False)
    pass2 = models.CharField(null=False)

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    photo = models.URLField(blank=True, null=True)
