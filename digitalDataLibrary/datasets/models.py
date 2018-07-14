from django.db import models


# Create your models here.
class data(models.Model):
    did = models.CharField(max_length=10, primary_key=True)
    time = models.IntegerField(max_length=30)
    category = models.CharField(max_length=20)
    tags = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(max_length=1)
    access = models.BooleanField()

