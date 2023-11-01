from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Schedules
from datetime import datetime, timedelta
from django.contrib.messages import constants
from django.contrib import messages
from .models import Schedules


@login_required
def schedules(request):
  if request.method == 'GET':
    user = request.user
    schedules = Schedules.objects.filter(user_id=user.id)
    print(schedules)
    return render(request, 'schedules.html', {'schedules': schedules})

@login_required
def new_schedule(request):
  if request.method == 'GET':
    return render(request, 'new_schedule.html')
  
  elif request.method == 'POST':
    hair = request.POST.get('hair')
    eyebrow = request.POST.get('eyebrow')
    beard = request.POST.get('beard')
    date = request.POST.get('date')
    time = request.POST.get('time')
    user = request.user
    
    has_hair = False
    has_beard = False
    has_eyebrow = False
    
    price = 0
    
    if hair != 'None':
      has_hair = True
      price += 30
      
    if beard != 'None':
      has_beard = True
      price += 15
      
    if eyebrow != 'None':
      has_eyebrow = True
      price += 10
      
    date_format = datetime.strptime(date, '%Y-%m-%d')
    yesterday = datetime.today() - timedelta(days=1)
    
    if date_format <= yesterday:
        messages.add_message(request, constants.ERROR, 'O dia não pode ter passado.')
        return redirect('/agendamentos/novo_agendamento')
          
    new_schedule = Schedules.objects.create(
      date=date,
      time=time,
      user_id=user,
      hair=has_hair,
      eyebrow=has_eyebrow,
      beard=has_beard,
      price=price
    )
    
    new_schedule.save()
    
    return redirect('/agendamentos/seus_agendamentos')
    
