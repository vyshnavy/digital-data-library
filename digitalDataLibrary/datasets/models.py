from django.db import models


# Create your models here.
class data(models.Model):
    did = models.CharField(max_length=10, primary_key=True)
    time = models.IntegerField()
    category = models.CharField(max_length=20)
    tags = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    access = models.BooleanField(default=True)
    path = models.CharField(max_length=200)
    click_count = models.IntegerField(default=0)
