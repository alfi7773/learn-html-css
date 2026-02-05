from django.db import models

from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Card(models.Model):
    title = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
