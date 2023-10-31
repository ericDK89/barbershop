from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
import time

def login(request):
  return render(request, 'login.html')

def register(request):
  if request.method == 'GET':
    return render(request, 'register.html')
  
  elif request.method == 'POST':
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    confirm_password=request.POST.get('confirm_password')
    
    if not password == confirm_password:
      messages.add_message(request, constants.ERROR, 'As senhas precisam ser iguais.')
      return redirect('/cadastro')
      
    if len(password) < 6:
      messages.add_message(request, constants.ERROR, 'A senha precisa ter 6 ou mais caracteres.')
      return redirect('/cadastro')
      
    if User.objects.filter(email=email).exists():
      messages.add_message(request, constants.WARNING, 'E-mail já cadastrado.')
      return redirect('/cadastro')
    
    try:
      user = User.objects.create_user(
        username=name, email=email, password=password
      )
      
      user.save()
    
      sucssefully = True
      
    except:
      sucssefully = False
      messages.add_message(request, constants.ERROR, 'Erro ao cadastrar o usuário.')
    
    return render(request, 'login.html', {'message': sucssefully})
  
