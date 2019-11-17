from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.landing,name='klooniLandingPage'),
    # url('^$',views.klooni_home,name='klooniHome'),
    # url(r'^search/', views.search_results,name='search_results'),
    # url(r'^article/(\d+)',views.article,name='article'),
    # url(r'^new/article$',views.new_article,name='new-article'),
    ]
if settings.DEBUG:
    urlpatterns
