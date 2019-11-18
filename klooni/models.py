from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField

#Profile model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(max_length = 200)


#Image Model
class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length =70)
    caption = models.CharField(max_length =700)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(blank=True)
    comments = models.CharField(max_length =200, blank=True)
    
    def save_image(self):
            self.save()
   
    class Meta:
        ordering = ['post_date']