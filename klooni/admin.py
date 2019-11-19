from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Comment)