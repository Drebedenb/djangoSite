from django.contrib import admin
from django.urls import path
from todo import views
from django.conf.urls import  include 

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('index.html', views.index),
    path('album.html', views.album),
    path('form.html', views.form),
    path('Login.html', views.login),
    path('meets.html', views.meets),
    path('create.html', views.create),
    path('thank-you.html', views.thank),
    path('todo/',include("todo.urls")),
]
