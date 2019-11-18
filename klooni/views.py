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
    profile = Profile.objects.all()
    return render(request,'klooni_pages/home.html', {'images':images, 'user':user, 'profile':profile})

#search feature
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'klooni_pages/search.html',{"message":message,"usernames": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'klooni_pages/search.html',{"message":message})