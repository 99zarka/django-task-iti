from django.db import models
from track.models import Track

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='students/images/', null=True, blank=True)
    date_of_birth = models.DateField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
