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
    
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        searched_articles = User.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})