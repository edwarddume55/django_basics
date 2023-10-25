
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery')
]
