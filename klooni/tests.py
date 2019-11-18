from django.test import TestCase
from .models import Profile, Image
from django.shortcuts import get_object_or_404


class ImageTestClass(TestCase):
    #set-up method
    def setUp(self):
        self.img = Image(id=1, name='imgOne',caption='capOne', likes=3, comments='clever!', profile_id=1)
        self.img.save_image()
        self.img.delete()
        
    #testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.img,Image))
    
    #testing the save_method
    def test_save_method(self):
        self.img.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)
        
    #testing the update_method
    # def test_update_method(self):
    #     self.img.update_image()

  #set-up method
    def setUp(self):
        self.img = Image(id=1, name='imgOne',caption='capOne', likes=3, comments='clever!', profile_id=1)
        self.img.save()
        self.img.delete()
        
    #testing the delete_method
    def test_delete_method(self):
        # img = get_object_or_404(Image,pk=1)
        img=Image.objects.filter(id=1).delete()
        self.assertTrue(len(img) == 1)
    
    #tear-down the instance
    def tearDown(self):
        Image.objects.all().delete()