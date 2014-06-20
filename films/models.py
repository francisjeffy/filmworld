from django.db import models


class Film(models.Model):
    title = models.TextField()
    director = models.ForeignKey('Director')


class Director(models.Model):
    name = models.TextField()