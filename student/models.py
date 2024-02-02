from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    ID = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='photos/', blank=True)
    grade = models.CharField(max_length=2)
    certificate = models.BooleanField(default=False)

    def __str__(self):
        return self.name
