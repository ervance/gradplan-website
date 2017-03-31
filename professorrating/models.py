from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Professor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    average_rating = models.IntegerField(blank=True)
    number_of_ratings = models.IntegerField(blank=True)

    def __str__(self):
        return self.first_name

class ClassRating(models.Model):
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    class_name = models.CharField(max_length=10)
    class_id = models.IntegerField(blank=True)
    rating = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.class_name
