from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField

#Profile model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(max_length = 200)
    
