from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()


class Drink(models.Model):
    title = models.CharField(max_length=256)
    imgurl = models.CharField(max_length=256)
    category = models.ManyToManyField(Category)