from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('google213d77350f25b686.html', views.google, name='google'),
]