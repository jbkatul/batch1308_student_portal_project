from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name