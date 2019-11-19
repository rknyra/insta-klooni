from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.landing,name='klooniLandingPage'),
    path('home/',views.home,name='klooniHome'),
    url('^search/', views.search_results,name='search_results'),
    url('^profile/',views.profilePage,name='klooniProfile'),
    path('like/<int:image_id>',views.likes,name='likes'),
    path('comment/<int:image_id>',views.comments,name='comments')
   ]
if settings.DEBUG:
    urlpatterns
