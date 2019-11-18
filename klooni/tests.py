from django.test import TestCase
from .models import Profile, Image

class ImageTestClass(TestCase):
    #set-up method
    def setUp(self):
        self.img = Image(name='imgOne', caption='capOne')
        self.img.save_image()
        
    #testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.img,Image))
    
    #testing the save_method
    def test_save_method(self):
        self.img.save_image()
        img = Image.objects.all()
        self.assertTrue(len(img) > 0)
    
    #tear-down the instance
    def tearDown(self):
        Image.objects.all().delete()