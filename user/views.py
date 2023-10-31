from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

def login(request):
  return render(request, 'login.html')

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  elif request.method == 'POST':
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    user = User.objects.create_user(
      username=name, email=email, password=password
    )
    
    user.save()
    
  return redirect('/')
