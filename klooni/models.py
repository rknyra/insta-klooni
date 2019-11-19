from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from pyuploadcare.dj.models import ImageField
from django.shortcuts import get_object_or_404

#Profile model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(max_length = 200)
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE, default=None)
    
    def save_profile(self):
        self.save()
            
    def update_profile(self):
        prof=Profile.objects.filter(id=Profile.id).update()
        
    def delete_image(self):
        prof=Profile.objects.filter(id=Profile.id).delete()
        
    
    @classmethod
    def profile(cls):
        profile = cls.objects.filter(id=Profile.id)
        return profile
    
    def __str__(self):
        return str(self.user)

#Image Model
class Image(models.Model):
    image = ImageField(blank=True, manual_crop="")
    name = models.CharField(max_length =70)
    caption = models.CharField(max_length =700)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(blank=True)
    comments = models.CharField(max_length =200, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    
    def save_image(self):
        self.save()
            
    def update_image(self):
        img=Image.objects.filter(id=Image.id).update()
        
    def update_caption(self):
        img=Image.objects.filter(id=Image.id).update()     
        
    def delete_image(self):
        # img = get_object_or_404(Image,pk=Image.id)
        img=Image.objects.filter(id=Image.id).delete()
   
    class Meta:
        ordering = ['post_date']
    
    @classmethod
    def images(cls):
        images = cls.objects.filter(id=Image.id)
        return images
    
    
    @classmethod
    def search_by_username(cls,profile):
        foundUser = cls.objects.filter(profile__username=profile)
        return foundUser
    
    @classmethod
    def filter_by_user_id(cls):
        photos = cls.objects.filter(id=user.user_id)
        return photos
    
    def __str__(self):
        return str(self.name)