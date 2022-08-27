from django.db import models

# Create your models here.

class Listmovie(models.Model):
    name=models.CharField(max_length=100)
    desc=model.TextField()
    rating=model.IntegerField