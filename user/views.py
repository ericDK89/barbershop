from django.http import HttpResponse
from django.shortcuts import render

def login(request):
  return render(request, 'login.html')

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')