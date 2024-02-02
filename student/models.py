from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    ID = models.CharField(max_length=10, unique=True)
    photo = models.ImageField(upload_to='photos/')
    grade = models.CharField(max_length=10)
    certificate = models.FileField(upload_to='certificates/')
