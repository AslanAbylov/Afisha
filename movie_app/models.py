from django.db import models

class Director(models.Model):
    name = models.TextField('')

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField('')
    duration = models.FloatField()

class Review(models.Model):
    text = models.TextField('')

