from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm

def index(request):
  return render(request, "index.html")

def login(request):
  return render(request, "Login.html")

def album(request):
  return render(request, "album.html")

def meets(request):
  news = Articles.objects.all()
  return render(request, "meets.html", {'news': news})

def create(request):
  error = ''
  if request.method == 'POST':
    form = ArticlesForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("index.html")
    else:
      error = 'Form is INCOCRRECT'

  
  form = ArticlesForm()

  data = {
    'form': form,
    'error': error
  }
  
  return render(request,"create.html",data)
