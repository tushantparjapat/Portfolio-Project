

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# from base.models import BaseModel
from datetime import datetime
import os
# Create your modelsf here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile" )
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100, blank= True,default="xyz")
    About = models.CharField(max_length=100, blank= True,default="xyz")

    def __str__(self) :
        return self.name