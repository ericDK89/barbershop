from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def login(request):
  if request.method == 'GET':
    return render(request, 'login.html')
  
  elif request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    user = authenticate(username=email, password=password)
  
    if user:
      auth_login(request, user)
      return redirect('/agendamentos/seus_agendamentos')
    else:
      messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
      return redirect('/')

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
        username=email, email=email, password=password, first_name=name
      )
      
      user.save()
    
      successfully = True
      
    except:
      successfully = False
      messages.add_message(request, constants.ERROR, 'Erro ao cadastrar o usuário.')
    
    return render(request, 'login.html', {'register_message': successfully})
  
