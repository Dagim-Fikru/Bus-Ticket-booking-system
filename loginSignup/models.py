from django.db import models
from sqlalchemy import VARCHAR

# Create your models here.
class Users(models.Model):
    # no id needed because the database automatically creat primary key
    username = models.CharField(max_length=150)
    email= models.CharField(max_length=30)
    password = models.IntegerField
