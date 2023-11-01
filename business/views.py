from django.shortcuts import render, redirect
from django.http import HttpResponse
from schedules.models import Schedules
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def business(request):
  all_schedules = Schedules.objects.all()
  return render(request, 'business.html', {'schedules': all_schedules})

@staff_member_required
def admin_cancel_schedule(request, schedule_id):
  schedule_to_remove = Schedules.objects.filter(id=schedule_id)
  schedule_to_remove.delete()
  return redirect('/administrativo')
