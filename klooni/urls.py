from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.landing,name='klooniLandingPage'),
    url('^home/',views.home,name='klooniHome'),
    url('^search/', views.search_results,name='search_results'),
    url('^profile/',views.profilePage,name='klooniProfile'),

    ]
if settings.DEBUG:
    urlpatterns
