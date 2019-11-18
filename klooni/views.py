from django.shortcuts import render
from django.contrib.auth import login, views, forms
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from django.contrib.auth.models import User


#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', {'form':form})

#home page
@login_required(login_url='/accounts/login')
def home(request):
    images = Image.objects.all()
    user = request.user.get_username()
    
    return render(request,'klooni_pages/home.html', {'images':images, 'user':user})