from django.shortcuts import render
from django.contrib.auth import login, views, forms
from django.contrib.auth.decorators import login_required
from .models import Profile, Image
from django.contrib.auth.models import User
from .forms import LikesNCommentsForm, UploadPicForm


#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', {'form':form})

#home page
@login_required(login_url='/accounts/login')
def home(request):
    form = LikesNCommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    profile = Profile.objects.all()
    comments_field = Image._meta.get_field('comments')
    likes_field = Image._meta.get_field('likes')
    
    if request.method == 'POST':
        form = LikesNCommentsForm(request.POST)
        if form.is_valid():
            likes = form.cleaned_data['likes']
            comment = form.cleaned_data['comment']
            
        else:
            form = LikesNCommentsForm()
                
    
    return render(request,'klooni_pages/home.html', {'images':images, 'user':user, 'profile':profile, 'form':form, 'comments_field':comments_field, 'likes_field':likes_field})

#search feature
@login_required(login_url='/accounts/login')
def search_results(request):
    
    if 'username' in request.GET and request.GET["username"]:
        form = forms.AuthenticationForm
        images = Image.objects.all()
        user = request.user.get_username()
        profile = Profile.objects.all()
        comments_field = Image._meta.get_field('comments')
        likes_field = Image._meta.get_field('likes')
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"
        # print(User.objects.get(username=search_term))
        photos = Image.objects.filter(profile=User.objects.get(username=search_term))


        return render(request, 'klooni_pages/search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'klooni_pages/search.html',locals())


#profile page
@login_required(login_url='/accounts/login')
def profilePage(request):
    images = Image.objects.all()
    user = request.user.get_username()
    current_user = request.user
    photos = Image.objects.filter(profile=current_user.id)
    profile = Profile.objects.all()
    comments_field = Image._meta.get_field('comments')
    likes_field = Image._meta.get_field('likes')
    
    return render(request,'klooni_pages/profile.html', locals())


#filter photos by user_id
# def filter_by_user_id(request, search_term):
#     photos = Image.filter_by_user_id(search_term)
#     message = f"{search_term}"
    
#     return render (request,'klooni_pages/profile.html',{"message":message,'photos': photos})