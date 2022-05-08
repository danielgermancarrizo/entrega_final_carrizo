from django.conf.urls import url
from web import views
from django.urls import path, include

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
   # path('about/', views.AboutPageView.as_view(), name='about'),
]