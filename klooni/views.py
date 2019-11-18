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
@login_required(login_url='/accounts/login')
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'klooni_pages/search.html',{"message":message,"usernames": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'klooni_pages/search.html',{"message":message})


#profile page
@login_required(login_url='/accounts/login')
def profilePage(request):
    images = Image.objects.all()
    user = request.user.get_username()
    current_user = request.user
    photos = Image.objects.filter(id=current_user.id)
    profile = Profile.objects.all()
    return render(request,'klooni_pages/profile.html', {'photos':photos, 'user':user, 'profile':profile, 'images': images})

# #filter photos by user_id
# def filter_by_user_id(request, search_term):
#     photos = Image.filter_by_user_id(search_term)
#     message = f"{search_term}"
    
#     return render (request,'klooni_pages/profile.html',{"message":message,'photos': photos})